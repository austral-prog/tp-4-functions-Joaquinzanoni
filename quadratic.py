import math

def roots(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        r1 = (-b + math.sqrt(discriminante)) / (2*a)
        r2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"({r1}, {r2})"
    elif discriminante == 0:
        r1 = -b / (2*a)
        return f"({r1})"
    else:
        return "( )"

def value_y(a, b, c, x):
    return a * x**2 + b * x + c

def to_string(a, b, c):
    if a == 0 and b == 0:
        return f"f(x) = {c}"
    if a == 0:
        return f"f(x) = {b} * X + {c}"
    if b == 0:
        return f"f(x) = {a} * X^2 + {c}"
    else:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"

def derivation(a, b, c):
    der_a = 2 * a
    if der_a == 0 and b == 0:
        return "f'(x) = 0"
    if der_a == 0:
        return f"f'(x) = {b}"
    if b == 0:
        return f"f'(x) = {der_a} * X"
    else:
        return f"f'(x) = {der_a} * X + {b}"