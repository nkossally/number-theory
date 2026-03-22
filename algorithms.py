def sieve_of_eratosthenes(n):
    """
    Finds all prime numbers up to n using the Sieve of Eratosthenes algorithm.
    """
    # Create a boolean array "prime[0...n]" and initialize
    # all entries it as True. A value in prime[i] will
    # finally be False if i is Not a prime, else True.
    prime = [True] * (n + 1)
    # 0 and 1 are not prime numbers
    if n >= 0:
        prime[0] = False
    if n >= 1:
        prime[1] = False

    p = 2
    # The optimization to stop at the square root of n is crucial for efficiency
    while (p * p <= n):
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
            # Update all multiples of p as False (composite)
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Collect all prime numbers
    prime_numbers = []
    for p in range(2, n + 1):
        if prime[p]:
            prime_numbers.append(p)
            
    return prime_numbers

    return "".join(reversed(remainder_list))

def get_expansion(n, base):
    res = []
    power = base
    while n != 0:
        remainder = n % power
        if remainder != 0:
            res.append(remainder)
        n -= remainder
        power *= base
    return res

def get_neg_base_expansion(n, base):
    neg_base = -base
    power = neg_base
    res = []
    while n != 0:
        remainder = n % power
        if remainder < 0:
            print(f"Negative remainder: {remainder}, adjusting to positive by adding {power}")
            remainder += abs(power)
        if remainder != 0:
            res.append(remainder)
        n -= remainder
        # print(f"n: {n}, remainder: {remainder}, power: {power}")

        power *= neg_base
    return res
        
def to_neg_base(f, base=-6):
    if f == 0:
        return "0"
    
    digits = []
    power = 1
    remainders = []
    # Use standard decimal digits, adjust for larger bases if needed
    numerals = "0123456789abcdefghijklmnopqrstuvwxyz" 
    
    while f != 0:
        # Calculate remainder (modulo operation in Python can return negative)
        remainder = f % base
        # Calculate quotient using integer division
        f //= base


        # Adjust for negative remainder, as digits must be non-negative (0 to |base|-1)
        if remainder < 0:
            remainder += abs(base)
            f += 1
            print(f"Negative remainder: {remainder},  {remainders}, {f}")

        if remainder != 0:
            remainders.append(remainder * power)
        power *= base
        print(f"f: {f}")
            
        digits.append(numerals[remainder])

    # The digits are collected in reverse order (least significant first)
    print(f"Remainders: {remainders}")
    return "".join(digits[::-1])




for i in range(14, 21):
    print(f"Expansion of {i} in base 6: {to_neg_base(i, -6)}")

