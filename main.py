from random import randint
from helper import compare, choose


def run_simulation(n, m, j, k, operation, num_trials):
    """
        N - bins
        M - balls
        J - which bin we are interested in
        K - how many balls fall into J's bin
    """
    success_trials = 0

    for i in range(num_trials):
        outcome = [randint(1, n) for _ in range(m)]
        if compare(outcome.count(j), k, operation):
            success_trials += 1

    return success_trials / num_trials


def compute_binomial(n, m, k):
    """
            N - bins
            M - balls
            K - bin has at most this # of balls
    """
    return sum([choose(m, i) * (1/n)**i * ((n - 1) / n)**(m - i) for i in range(k + 1)])


def simulate_experiment():
    n = 5  # bins
    m = 7  # balls
    num_trials = 10000000

    p_1_bin_has_exactly_3_balls = run_simulation(n, m, 1, 3, '==', num_trials)
    estimated_p_3_bin_has_at_least_3_balls = run_simulation(n, m, 3, 3, '>=', num_trials)
    exact_p_3_bin_has_at_least_3_balls = 1 - compute_binomial(n, m, 2)

    print(f'estimated P[1st bin has exactly 3 balls] = {p_1_bin_has_exactly_3_balls}')
    print(f'estimated P[3rd bin has at least 3 balls] = {estimated_p_3_bin_has_at_least_3_balls}')
    print(f'Exact P[3rd bin has at least 3 balls] = {exact_p_3_bin_has_at_least_3_balls} ')


simulate_experiment()



