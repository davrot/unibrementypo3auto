from bib.shorten_authorname import shorten_authorname
import pandas as pd


def combine_names(names):
    name = names[0]
    if len(names) > 1:
        for i in names[1:]:
            name += str(" and ") + i

    return name


def fix_author(name, db):
    name = shorten_authorname(name)

    for idx in db.keys():
        if idx == name:
            return idx

        for id in db[idx]:
            if id == name:
                return idx

    return name


def make_dataframe(
    entry: dict, author_json: dict, full_type_list: list[str], index_number: int
):
    # Check if everything is there
    if "ENTRYTYPE" not in entry.keys():
        return None

    if entry["ENTRYTYPE"] not in full_type_list:
        return None

    if "title" not in entry.keys():
        return None

    if "year" not in entry.keys() and "date" not in entry.keys():
        return None

    if "author" not in entry.keys() and "editor" not in entry.keys():
        return None

    # Title
    title = str(entry["title"]).lstrip().rstrip()

    # Year
    if "year" in entry.keys():
        year = str(entry["year"]).lstrip().rstrip()
    else:
        year = str(entry["date"]).split("-")[0].lstrip().rstrip()

    # Authors
    if "author" in entry.keys():
        author = entry["author"]
    else:
        author = []
        for e_id in entry["editor"]:
            author.append(e_id["name"])

    for i in range(0, len(author)):
        author[i] = fix_author(author[i], author_json)
    author_string = combine_names(author)

    # DOI
    doi: str = ""
    if "doi" in entry.keys():
        doi = str(entry["doi"]).lstrip().rstrip()

    # Journal name
    journal: str = ""
    if "journal" in entry.keys():
        journal = str(entry["journal"]).lstrip().rstrip()
    if "journaltitle" in entry.keys():
        journal = str(entry["journaltitle"]).lstrip().rstrip()
    elif "booktitle" in entry.keys():
        journal = str(entry["booktitle"]).lstrip().rstrip()
    elif "note" in entry.keys():
        journal = str(entry["note"]).lstrip().rstrip()
    elif "school" in entry.keys():
        journal = str(entry["school"]).lstrip().rstrip()
    elif "publisher" in entry.keys():
        journal = str(entry["publisher"]).lstrip().rstrip()

    title = title.replace("{", "").replace("}", "")
    journal = (
        journal.replace("\\textbackslash", "\\")
        .replace("Publication Title: ", "")
        .replace("\\&", "&")
    )

    dataframe: None | dict = dict(
        year=year,
        title=title,
        author=author_string,
        doi=doi,
        journal=journal,
    )

    return pd.DataFrame(dataframe, index=[index_number])
