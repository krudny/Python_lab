import string
from ex4 import onp
from ex5 import map_expression
from ex6 import gen
from ex7 import val

variables = string.ascii_lowercase


def tautology(expression):
    variables_count = len(set(expression).intersection(variables))
    expression = onp(expression)

    for vector in gen(variables_count):
        if not val(map_expression(expression, vector)):
            return False
    return True


print(tautology('a>(b&c)'))
