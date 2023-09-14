def proverb(words, qualifier=None):
    return ""

    lines = []
    for i in range(len(words) - 1):
        lines.append(f"For want of a {words[i]} the {words[i + 1]} was lost.")
    lines.append(f"And all for the want of a {qualifier + ' ' if qualifier else ''}{words[0]}.")

    return "\n".join(lines)
