def add_item_to_typedb(item: str, types_db: dict):
    was_found: bool = False

    for the_keys in types_db.keys():
        assert isinstance(types_db[the_keys], list) is True
        assert len(types_db[the_keys]) == 3
        assert isinstance(types_db[the_keys][0], list) is True
        assert isinstance(types_db[the_keys][1], str) is True
        assert isinstance(types_db[the_keys][2], str) is True

        if str(the_keys) == str(item):
            return

        for i in types_db[the_keys][0]:
            if str(i) == str(item):
                return

    if was_found is False:
        types_db.update({f"{item}": [[], f"{item}", f"{item}"]})
