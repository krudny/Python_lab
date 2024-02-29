from ex2 import bracket
from ex3 import bal


def onp(expression):
    expression = bracket(expression)

    if p := bal(expression, '>'):
        return onp(expression[:p]) + onp(expression[p + 1:]) + expression[p]
    if p := bal(expression, '|&'):
        return onp(expression[:p]) + onp(expression[p + 1:]) + expression[p]

    return expression
