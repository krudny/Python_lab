import string
from ex2 import bracket

variables = string.ascii_lowercase


def alg(expression):
    stack = []

    for char in expression:
        if char in variables:
            stack.append(char)
        else:
            p = stack.pop()
            q = stack.pop()

            stack.append('(' + q + char + p + ')')

    return bracket(stack[0])
