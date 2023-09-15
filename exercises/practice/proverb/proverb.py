def proverb(inputs, qualifier=None):
    generated_proverb = ""
    
    for i in range(len(inputs) - 1):
        generated_proverb += f"For want of a {inputs[i]} the {inputs[i+1]} was lost.\n"
    
    if qualifier:
        generated_proverb += f"And all for the want of a {qualifier} {inputs[0]}."
    else:
        generated_proverb += f"And all for the want of a {inputs[0]}."
    
    return generated_proverb