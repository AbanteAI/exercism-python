def proverb(*items, qualifier=None):
    if not items:
        return ""
    lines = []
    for i in range(len(items) - 1):
        lines.append(f"For want of a {items[i]} the {items[i+1]} was lost.")
    if qualifier:
        lines.append(f"And all for the want of a {qualifier}.")
    else:
        lines.append(f"And all for the want of a {items[0]}.")
    return "\n".join(lines)
        return ""
    lines = []
    for i in range(len(items) - 1):
        lines.append(f"For want of a {items[i]} the {items[i+1]} was lost.")
    if qualifier:
        lines.append(f"And all for the want of a {qualifier}.")
    else:
        lines.append(f"And all for the want of a {items[0]}.")
    return "\n".join(lines)
        return ""
    lines = []
    for i in range(len(items) - 1):
        lines.append(f"For want of a {items[i]} the {items[i+1]} was lost.")
    if qualifier:
        lines.append(f"And all for the want of a {qualifier}.")
    else:
        lines.append(f"And all for the want of a {items[0]}.")
    return "\n".join(lines)
