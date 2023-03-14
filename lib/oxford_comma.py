def oxford_comma(items):
    if (len(items) == 2):
        return " and ".join(items)
    elif (len(items) >= 3):
        last_item = items.pop()
        return ", ".join(items) + f", and {last_item}"
    else:
        return "".join(items)

print(oxford_comma(["fiddleheads", "okra", "kohlrabi"]))