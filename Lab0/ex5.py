import string

operators = '|&>'
variables = string.ascii_lowercase


def map_expression(expression, vector):
    for char, value in zip(list(sorted(set(expression).intersection(variables))), vector):
        expression = expression.replace(char, value)

    return expression


