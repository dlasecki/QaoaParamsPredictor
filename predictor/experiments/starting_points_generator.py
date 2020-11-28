import math
import random


def generate_starting_points(p_params, num_of_starting_points):
    points = {}
    for p in p_params:
        points_p = generate_starting_points_p(p, num_of_starting_points)
        points[p] = points_p
    return points


def generate_starting_points_p(p, num_of_starting_points):
    starting_points = []
    for i in range(num_of_starting_points):
        betas = _get_random_betas(p)
        gammas = _get_random_gammas(p)
        starting_points.append(betas+gammas)

    return starting_points


def _get_random_betas(p):
    beta_integers = random.sample(range(0, 1001), p)
    betas = [math.pi * beta_integer / 1000.0 for beta_integer in beta_integers]
    return betas


def _get_random_gammas(p):
    gamma_integers = random.sample(range(0, 1001), p)
    gammas = [2 * math.pi * gamma_integer / 1000.0 for gamma_integer in gamma_integers]
    return gammas
