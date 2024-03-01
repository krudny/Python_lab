from ex1 import check
from ex2 import bracket
from ex3 import bal
from ex4 import onp
from ex5 import map_expression
from ex6 import gen
from ex7 import val
from ex8 import tautology
from ex9 import alg


def test_check():
    assert check('a>b>c&a') is True
    assert check('(a>(b&c)') is False
    assert check('a&b|c') is True
    assert check('a&b|c>') is False
    assert check('a|b&c') is True
    assert check('a|b&c>d') is True


def test_bracket():
    assert bracket('a>b>c&a') == 'a>b>c&a'
    assert bracket('(a>(b&c)') == '(a>(b&c)'
    assert bracket('a&b|c') == 'a&b|c'
    assert bracket('((((a))))') == 'a'
    assert bracket('a|b&c') == 'a|b&c'
    assert bracket('(a|b&c>d)') == 'a|b&c>d'


def test_bal():
    assert bal('a>b>c&a', '>') == 3
    assert bal('(a>(b&c))', '>') is None
    assert bal('a&b|c', '>') is None
    assert bal('a&b|c>', '>') == 5
    assert bal('a>(b>c)', '>') == 1


def test_onp():
    assert onp('a>b>c&a') == 'ab>ca&>'
    assert onp('(a>(b&c))') == 'abc&>'
    assert onp('a&b|c') == 'ab&c|'
    assert onp('a|b&c') == 'ab|c&'
    assert onp('(a>(b|c))') == 'abc|>'


def test_map_expression():
    assert map_expression('ab>ca&>', '000') == '00>00&>'
    assert map_expression('ab>ca&>', '001') == '00>10&>'
    assert map_expression('ab>ca&>', '010') == '01>00&>'
    assert map_expression('ab>ca&>', '011') == '01>10&>'
    assert map_expression('ab>dca&>', '1001') == '10>101&>'


def test_gen():
    assert list(gen(3)) == ['000', '001', '010', '011', '100', '101', '110', '111']
    assert list(gen(2)) == ['00', '01', '10', '11']
    assert list(gen(1)) == ['0', '1']
    assert list(gen(0)) == ['']


def test_val():
    assert val('00>00&>') == 0
    assert val('00>10&>') == 0
    assert val('01>00&>') == 0
    assert val('101>&') == 1
    assert val('10>101&>') == 0


def test_tautology():
    assert tautology('a>a') is True
    assert tautology('a>a>b') is False
    assert tautology('a&b|c') is False
    assert tautology('a|b&c') is False
    assert tautology('a|b&c') is False


def test_alg():
    assert alg('ab&') == 'a&b'
    assert alg('ab>') == 'a>b'
    assert alg('abc|>') == 'a>(b|c)'
    assert alg('ab>ca&>') == '(a>b)>(c&a)'







