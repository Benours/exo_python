import math


def trinome(a, b, c):
    delta = math.pow(b, 2) - 4 * a * c
    if delta < 0:
        return None
    elif delta == 0:
        return -b / (2 * a)
    else:
        return (-b - math.sqrt(delta)) / (2 * a), (-b + math.sqrt(delta)) / (2 * a)


print(trinome(1, -3, 2))
print(trinome(1, -2, 1))
print(trinome(1, 1, 1))
