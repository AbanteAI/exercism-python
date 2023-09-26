class StackUnderflowError(Exception):
    pass


def evaluate(input_data):
    input_data = " ".join(input_data)
    stack = []
    custom_words = {}
    
    def check_stack_size(n):
        if len(stack) < n:
            raise StackUnderflowError("Stack underflow")

    def perform_operation(op):
        check_stack_size(2)
        b = stack.pop()
        a = stack.pop()
        result = op(a, b)
        stack.append(result)

    def execute_custom_word(word):
        if word in custom_words:
            definition = custom_words[word]
            evaluate(definition)
        else:
            stack.append(int(word))

    i = 0
    while i < len(words):
        word = words[i].lower()
        
        if word == ":":
            custom_word = words[i + 1].lower()
            definition_start = i + 2
            definition_end = words.index(";", definition_start)
            custom_words[custom_word] = words[definition_start:definition_end]
            i = definition_end
        elif word == "+":
            perform_operation(lambda a, b: a + b)
        elif word == "-":
            perform_operation(lambda a, b: a - b)
        elif word == "*":
            perform_operation(lambda a, b: a * b)
        elif word == "/":
            perform_operation(lambda a, b: a // b)
        elif word == "dup":
            check_stack_size(1)
            stack.append(stack[-1])
        elif word == "drop":
            check_stack_size(1)
            stack.pop()
        elif word == "swap":
            check_stack_size(2)
            stack[-2], stack[-1] = stack[-1], stack[-2]
        elif word == "over":
            check_stack_size(2)
            stack.append(stack[-2])
        else:
            execute_custom_word(word)

        i += 1

    return stack
