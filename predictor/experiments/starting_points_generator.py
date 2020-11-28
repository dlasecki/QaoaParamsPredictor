def generate_starting_points(p_params, num_of_starting_points):
    points = {}
    for p in p_params:
        points_p = generate_starting_points_p(p, num_of_starting_points)
        points[p] = points_p
    return points


def generate_starting_points_p(p, num_of_starting_points):
    return []
