def shorten_authorname(input: str) -> str:
    temp = input.split(",")
    name: str = temp[0].lstrip().rstrip() + str(",")
    temp = temp[1].lstrip().rstrip().split(" ")
    for i in temp:
        if len(i) > 0:
            first_letter = i.upper()[0]
            if first_letter.isalpha() is True:
                name += str(" ") + first_letter + str(".")
    return name
