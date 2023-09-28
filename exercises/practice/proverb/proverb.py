def proverb(*items, qualifier=None):
    lines = [f"For want of a {items[i]} the {items[i + 1]} was lost." for i in range(len(items) - 1)]
    if qualifier:
        last_line = f"And all for the want of a {qualifier} {items[0]}."
    else:
        last_line = f"And all for the want of a {items[0]}."
    return "\n".join(lines + [last_line])