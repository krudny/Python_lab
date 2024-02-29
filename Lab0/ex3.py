def bal(expression, operator):
    bracket_count = 0

    for i in range(len(expression) - 1, -1, -1):
        if expression[i] == '(':
            bracket_count += 1
        elif expression[i] == ')':
            bracket_count -= 1
        elif expression[i] in operator and bracket_count == 0:
            return i

    return None

