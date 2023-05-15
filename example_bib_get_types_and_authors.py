from bib.customizations import customizations_tajd
from bib.unique_type_list import unique_type_list
from bib.unique_author_list import unique_author_list
from bib.load_bib_file import load_bib_file

filename_bib: str = "neuro.bib"


bib_database = load_bib_file(filename_bib, customizations_tajd)
unique_types = unique_type_list(bib_database)
print("These types have been found:")
print(unique_types)
print()

unique_authors = unique_author_list(bib_database)
print("These authors have been found:")
print(unique_authors)
