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