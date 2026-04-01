def euclidean_algorithm(a, b):
    """Calculate the greatest common divisor of a and b using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

print(euclidean_algorithm(48, 18))  # Output: 6
print(euclidean_algorithm(18, 48))  # Output: 6