from bib.shorten_authorname import shorten_authorname


def unique_author_list(bib_database):
    temp_authors = []
    for idx in range(0, len(bib_database.entries)):
        if "author" in bib_database.entries[idx].keys():
            for temp_entry in bib_database.entries[idx]["author"]:
                temp_authors.append(shorten_authorname(temp_entry))
        else:
            print(f"Author is missing. Entry-ID:{idx}")

    unique_autors = list(set(temp_authors))
    unique_autors.sort()
    return unique_autors
