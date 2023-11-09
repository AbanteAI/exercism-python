def proverb(*items, qualifier=''):
    lines = []
    if len(items) > 1:
        for i in range(len(items) - 1):
            line = f"For want of a {items[i]} the {items[i+1]} was lost."
            lines.append(line)
    if qualifier:
        qualifier += ' '
    final_line = f"And all for the want of a {qualifier}{items[0]}."
    lines.append(final_line)
    return '\n'.join(lines)
