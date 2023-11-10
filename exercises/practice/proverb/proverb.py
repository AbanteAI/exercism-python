def proverb(*items, qualifier=''):
    lines = []
    if len(items) > 1:
        for i in range(len(items) - 1):
            lines.append(f"For want of a {items[i]} the {items[i+1]} was lost.")
    qualifier = f"{qualifier} " if qualifier else ""
    lines.append(f"And all for the want of a {qualifier}{items[0]}.")
    return '\n'.join(lines)