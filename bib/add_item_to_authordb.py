def add_item_to_authordb(item: str, author_db: dict):
    was_found: bool = False

    for the_keys in author_db.keys():
        assert isinstance(author_db[the_keys], list) is True

        if str(the_keys) == str(item):
            return

        for i in author_db[the_keys]:
            print(i)
            if str(i) == str(item):
                return

    if was_found is False:
        author_db.update({f"{item}": []})
