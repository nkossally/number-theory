from gcd_euclidean_algorithm import get_gcd_euclidean_algorithm

def get_congruences(a, b, m):
    """Returns a list of all integers x such that ax ≡ b (mod m)."""
    divisor = get_gcd_euclidean_algorithm(a, m)
    if b % divisor != 0:
        return []
    curr = 0
    while curr < m and a *curr %m != b:
        curr += 1
    res = []
    for i in range(divisor):
        res.append(curr + i * m//divisor)
    return res

print(get_congruences(2, 3, 5))  
print(get_congruences(2, 3, 31))  
print(get_congruences(4, 12, 32))  
print(get_congruences(3, 7, 15))  
