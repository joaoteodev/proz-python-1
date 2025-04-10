def get_text_list(list_items):
    size = len(list_items)
    text = ""

    for x in range(size):
        if x == size - 2:
            text += f"{list_items[x]} e "
            continue

        if x == size - 1:
            text += f"{list_items[x]}"
            continue

        text += f"{list_items[x]}, "

    return text