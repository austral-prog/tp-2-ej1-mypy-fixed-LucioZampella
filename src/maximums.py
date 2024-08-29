def max_of_two(x: float, y: float) -> float:
    """Given x and y, that are 2 numbers, return the biggest number."""
    biggest: float = x
    if x >= y:
        return biggest
    else:
        biggest = y
        return biggest


def max_of_three(x: float, y: float, z: float) -> float:
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    biggest = x
    if y > biggest:
        biggest = y
    if z > biggest:
        biggest = z
    return biggest
