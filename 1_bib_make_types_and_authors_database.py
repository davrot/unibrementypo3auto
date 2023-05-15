from bib.customizations import customizations_tajd
from bib.unique_type_list import unique_type_list
from bib.unique_author_list import unique_author_list
from bib.load_bib_file import load_bib_file
from bib.add_item_to_typedb import add_item_to_typedb
from bib.add_item_to_authordb import add_item_to_authordb

import os
import json

filename_bib: str = "neuro.bib"
bib_database = load_bib_file(filename_bib, customizations_tajd)


# Types ->
filename_types_db: str = "types_db.json"

# load type database, in the case it exists
if os.path.exists(filename_types_db) is True:
    with open(filename_types_db, "r") as file:
        try:
            types_db: dict = json.load(file)
        except json.decoder.JSONDecodeError:
            types_db = dict()
else:
    types_db = dict()

unique_types = unique_type_list(bib_database)

# Add the items to the database
for item in unique_types:
    add_item_to_typedb(item, types_db)

# Save type database
with open(filename_types_db, "w") as file:
    json.dump(types_db, file)

# <- Types

# Author ->
filename_authors_db: str = "authors_db.json"

# load type database, in the case it exists
if os.path.exists(filename_authors_db) is True:
    with open(filename_authors_db, "r") as file:
        try:
            author_db: dict = json.load(file)
        except json.decoder.JSONDecodeError:
            author_db = dict()
else:
    author_db = dict()

unique_authors = unique_author_list(bib_database)

# Add the items to the database
for item in unique_authors:
    add_item_to_authordb(item, author_db)

# Save type database
with open(filename_authors_db, "w") as file:
    json.dump(author_db, file)

# <- Author
