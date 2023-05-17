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
If you want to use another bib filename, you need to change it in 1_bib_make_types_and_authors_database.py under 
```
filename_bib: str = "neuro.bib"
```

### types_db.json 

An entry looks like this:
```
"article": [[], "article", "article"]
```
Beside the key, there are three components. 
1. An list with alternative keys. In the case we want to fuse several keys into one category. 
2. The German headline
3. The English headline

Thus we want to change it into:
```
"article": [[], "Artikel", "Article"]
```
### authors_db.json 

An entry looks like this:
```
"Pawelzik, K.": [],
```
The key is later used for generating the author name in the html lists. Again a list with alternative author names follows.

Since this entry is wrong, we fix it by:
```
"Pawelzik, K. R.": ["Pawelzik, K."],
```
# make_typo3_publication_template.py

This program builds a template for the presentation of the bibliographie on a given page id. Change page_id: int = 59585 accordingly.
It uses the information from the types_db.json.






