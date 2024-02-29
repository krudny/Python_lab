from ex1 import check


def bracket(expression):
    if expression[0] == '(' and expression[-1] == ')' and check(expression[1:-1]):
        return bracket(expression[1:-1])

    return expression
