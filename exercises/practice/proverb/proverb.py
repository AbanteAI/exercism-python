def proverb(items, *, qualifier=''):
    lines = []
    for i in range(len(items) - 1):
        lines.append(f"For want of a {items[i]} the {items[i+1]} was lost.")
    if items:
        qualifier = f"{qualifier} " if qualifier else ""
        lines.append(f"And all for the want of a {qualifier}{items[0]}.")
    return lines