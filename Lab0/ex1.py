import string

variables = string.ascii_lowercase+'0'+'1'
operators = '|&>^'


def check(expression):
    state = True
    bracket_count = 0

    for char in expression:
        if state:
            if char == '(':
                bracket_count += 1
            elif char in variables:
                state = False
            else:
                return False
        else:
            if char == ')':
                bracket_count -= 1
            elif char in operators:
                state = True
            else:
                return False

        if bracket_count < 0:
            return False

    return bracket_count == 0 and not state


