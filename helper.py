from math import factorial


def compare(a, b, operation):
    assert operation == '==' or operation == '>=', 'operation must be == or >=!'

    if operation == '==':
        return a == b
    else:
        return a >= b


def choose(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))
