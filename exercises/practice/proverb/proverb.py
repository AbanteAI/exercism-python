def proverb(inputs):
    lines = []
    for i in range(len(inputs) - 1):
        line = f"For want of a {inputs[i]} the {inputs[i+1]} was lost."
        lines.append(line)
    if inputs:
        lines.append(f"And all for the want of a {inputs[0]}.")
    return "\n".join(lines)
        line = f"For want of a {inputs[i]} the {inputs[i+1]} was lost."
        lines.append(line)
    if inputs:
        lines.append(f"And all for the want of a {inputs[0]}.")
    return "\n".join(lines)