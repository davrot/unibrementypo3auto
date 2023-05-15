# Uni-Bremen Typo3 Automatization Tools
## Pip packages

```
pip install selenium
pip install webdriver-manager
pip install numpy
```

For the bib tools:

```
pip3 install bibtexparser
pip3 install pandas
```

## How to use the typo3 examples:
* Change user name in username.json
* Change the page id and content id to something you can and want to work ong


## 1_bib_make_types_and_authors_database.py

Running this program produces (or updates) two databases:
* types_db.json : Containing the list of the types of publications. 
* authors_db.json : Containing the list of the authors.

If you want to remove an entry from these databases, you need to delete it yourself. 

### types_db.json 

An entry looks like this:
'''
"article": [[], "article", "article"]
'''





