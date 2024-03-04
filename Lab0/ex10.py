import string
from ex2 import bracket
from ex4 import onp
from ex6 import gen
from ex7 import val

variables = string.ascii_lowercase


def negate(value):
    return 1 - value


def map_expression(expression, values):
    for char in list(sorted(set(expression).intersection(variables))):
        expression = expression.replace(char, values[char])

    return expression


def prepare_expression(expression):
    result = []
    to_negate = []
    brackets = 0
    for i in range(len(expression)):
        if expression[i] == '~' and expression[i+1] == '(':
            brackets += 1
            for j in range(i+2, len(expression)):
                if expression[j] == '(':
                    brackets += 1
                if expression[j] == ')':
                    brackets -= 1

                    if brackets == 0:
                        to_negate.append(expression[i+1:j+1])
                        break
        elif expression[i] == '~':
            to_negate.append(expression[i+1:i+2])

    variables_count = len(set(expression).intersection(variables))

    for vector in gen(variables_count):
        dp = {}
        for i, char in enumerate(set(expression).intersection(variables)):
            dp[char] = vector[i]

        new_expression = expression
        for sub_expression in to_negate:
            new_expression = new_expression.replace('~' + sub_expression, str(negate(int(val(map_expression(onp(bracket(sub_expression)), dp))))))

        new_expression = new_expression.replace("~", "")

        new_expression = map_expression(onp(bracket(new_expression)), dp)

        result.append((vector, str(val(new_expression))))

    return result


def equivalence(expression1, expression2):

    return prepare_expression(expression1) == prepare_expression(expression2)


# print(equivalence('a>b', '~a|b'))
# print(equivalence('a>b', '~a&b'))
# print(equivalence('a|(~a&b)', 'a|b'))
# print(equivalence('a>~(b|c)', '~(a&(b|c))'))
# print(equivalence('(a|~b)>(a&b)', '(a&b)|(a&b)'))
print(equivalence('~(a^b)|(c>d)', '(a&c)|(~a&~b)|~c|d'))
