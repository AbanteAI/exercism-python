def proverb(*items, qualifier=None):
    lines = []
    for i in range(len(items) - 1):
        lines.append(f"For want of a {items[i]} the {items[i + 1]} was lost.")
    if qualifier:
        final_line = f"And all for the want of a {qualifier} {items[0]}."
    else:
        final_line = f"And all for the want of a {items[0]}."
    lines.append(final_line)
    return lines