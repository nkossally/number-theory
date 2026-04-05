import math
def get_inverse(a, m):
    for num in range(m):
        if (a * num) % m == 1:
            return num
    return None

def solve_chinese_remainder_theorem(nums, residues):
    product = math.prod(nums)
    res = 0
    for i, num in enumerate(nums):
        residue = residues[i]
        curr_prod = product // num
        inverse = get_inverse(curr_prod, num)
        res += residue * inverse * curr_prod
    res = res % product


    return res




def solve_chinese_remainder_theorem_2(congruences):
    """Solves a system of congruences using the Chinese Remainder Theorem."""
    M = 1
    for _, m in congruences:
        M *= m

    solution = 0
    for a, m in congruences:
        Mi = M // m
        yi = pow(Mi, -1, m)
        solution += a * Mi * yi

    return solution % M 

print(solve_chinese_remainder_theorem([2, 5, 7, 9], [1, 2, 3, 4]))