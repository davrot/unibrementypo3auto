def unique_type_list(bib_database):
    temp_types = []
    for idx in range(0, len(bib_database.entries)):
        if "ENTRYTYPE" in bib_database.entries[idx].keys():
            entry = bib_database.entries[idx]
            entry_type: str = str(entry["ENTRYTYPE"]).lstrip().rstrip()
            temp_types.append(entry_type)
    unique_types = list(set(temp_types))
    unique_types.sort()
    return unique_types
