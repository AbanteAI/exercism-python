def proverb(inputs, qualifier=""):
    lines = []
    for i in range(len(inputs) - 1):
        lines.append(f"For want of a {inputs[i]} the {inputs[i+1]} was lost.")
    if inputs:
        lines.append(f"And all for the want of a {qualifier} {inputs[0]}.")
    return lines