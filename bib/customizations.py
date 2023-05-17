import bibtexparser


def customizations_tajd(record):
    record = bibtexparser.customization.type(record)
    record = bibtexparser.customization.author(record)
    record = bibtexparser.customization.journal(record)
    record = bibtexparser.customization.doi(record)
    return record


def customizations_tae(record):
    record = bibtexparser.customization.type(record)
    record = bibtexparser.customization.author(record)
    record = bibtexparser.customization.editor(record)
    return record
