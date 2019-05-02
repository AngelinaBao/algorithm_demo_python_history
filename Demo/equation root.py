import math

def quadratic(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        raise TypeError("delta is negative! No root!")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
    return x1, x2

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))