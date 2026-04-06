import math

def solve_system(a, b, c, d, e, f, m):
    """
    solves the system
    ax +by = e mod(m)
    cx + dy = f mod(m)
    """
    determinant = a * d - b * c
    inverse = get_inverse(determinant, m)
    if inverse == None:
        return None
    x = inverse * (d * e - b *f) % m
    y = inverse * (a *f - c *e) % m
    return (x, y)

def get_inverse(i, m):
    if math.gcd(i, m) != 1:
        return None
    curr = 0
    while curr < m and curr  * i % m != 1:
        curr += 1
    return curr

print(solve_system(3, 4, 2, 5, 5, 7, 13))