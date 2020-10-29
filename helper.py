from math import factorial


def compare(outcome, b, value, operation, n):
    """
        :param outcome: one outcome of the experiment we are performing
        :param b: used only for '==' and '>=' where we look at single bin. Denotes the bin that we are examining.
        :param value: Denotes the # of balls that we want to check the bin(s) for
        :param operation: determines the way we compare the values we provided
        :param n: number of bins. Needed only for 'count' since there we check every bin
        :return: returns whether a condition is true
    """
    assert operation == '==' or operation == '>=' or operation == 'count', 'operation must be == or >=! or count!'

    if operation == '==':
        return outcome.count(b) == value
    elif operation == '>=':
        return outcome.count(b) >= value
    elif operation == 'count':
        for i in range(1, n + 1):
            if outcome.count(i) == value:
                return True
        return False


def choose(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))
