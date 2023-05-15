import bibtexparser


def load_bib_file(filename_bib: str, customizations):
    # Load the bib file:
    with open(filename_bib, mode="r") as file:
        file_content: str = file.read()

    parser = bibtexparser.bparser.BibTexParser()
    parser.customization = customizations
    parser.ignore_nonstandard_types = False

    bib_database = bibtexparser.loads(file_content, parser=parser)

    return bib_database
