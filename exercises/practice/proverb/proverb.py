def proverb(*items, qualifier=""):
    lines = []
    for i in range(len(items) - 1):
        lines.append(f"For want of a {items[i]} the {items[i+1]} was lost.")
    if items:
        lines.append(f"And all for the want of a {qualifier} {items[0]}.")
    return lines
    lines = []
    for i in range(len(items) - 1):
        lines.append(f"For want of a {items[i]} the {items[i+1]} was lost.")
    if items:
        lines.append(f"And all for the want of a {items[0]}.")
    return lines