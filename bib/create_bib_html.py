from bib.customizations import customizations_tae
from bib.load_bib_file import load_bib_file
from bib.make_dataframe import make_dataframe

import pandas as pd
import json
import html


def filter_string(input):
    return str(html.escape(input).encode("ascii", "xmlcharrefreplace").decode())


def format_entry(entry) -> str:
    output: str = (
        str("<tr><td>")
        + entry["author"]
        + str(" (")
        + str(int(entry["year"]))
        + str(") ")
    )
    if len(entry["doi"]) == 0:
        output += str("<b>") + filter_string(entry["title"]) + str("</b> ")
    else:
        output += (
            str('<b><a href="')
            + entry["doi"]
            + str('">')
            + filter_string(entry["title"])
            + str("</a></b> ")
        )
    output += filter_string(entry["journal"]) + "</td></tr>"
    output = output.replace("{", "<i>")
    output = output.replace("}", "</i>")

    return output


def create_bib_html(user_string: str, type_string: str, filename_bib: str) -> str:
    bib_database = load_bib_file(filename_bib, customizations_tae)

    with open("types_db.json", "r") as file:
        type_dict = json.load(file)

    with open("authors_db.json", "r") as file:
        author_dict = json.load(file)

    # Make a list of all the bib types we need
    full_type_list: list = []
    full_type_list.append(type_string)

    for t_id in type_dict.keys():
        assert len(type_dict[t_id]) == 3
        if type_string == t_id:
            for i in type_dict[t_id][0]:
                full_type_list.append(i)

    # Make pandas data base for only the selected bib type
    pf_data_frames = None
    for i in range(0, len(bib_database.entries)):
        df = make_dataframe(bib_database.entries[i], author_dict, full_type_list, i)

        if (pf_data_frames is None) and (df is not None):
            pf_data_frames = df
        elif df is not None:
            pf_data_frames = pd.concat((pf_data_frames, df))

    if pf_data_frames is None:
        return ""

    # Debuging:
    # pf_data_frames.to_excel("excel_1.xlsx")

    # Filter and sort the pandas data base
    if len(user_string) > 0:
        pf_data_frames = pf_data_frames.where(
            pf_data_frames["author"].str.contains(user_string)
        ).dropna()

    pf_data_frames = pf_data_frames.sort_values(
        ["year", "author"], ascending=[False, True]
    )

    if len(pf_data_frames) == 0:
        return ""

    # Debuging:
    # pf_data_frames.to_excel("excel_2.xlsx")

    # Build html
    output: str = ""
    actual_year: int = int(pf_data_frames.iloc[0]["year"])
    output += str("<h3>") + f"{actual_year}" + str("</h3>\n")
    output += str("<table>")

    for entry_id in range(0, len(pf_data_frames)):
        if actual_year != int(pf_data_frames.iloc[entry_id]["year"]):
            actual_year = int(pf_data_frames.iloc[entry_id]["year"])
            output += str("</table>")
            output += str("\n<h3>") + f"{actual_year}" + str("</h3>\n")
            output += str("<table>")

        output += format_entry(pf_data_frames.iloc[entry_id])
    output += str("</table>")

    return output
