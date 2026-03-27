

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

def get_expansion_2(n, base):
    num = n
    res = []
    power = base
    while num != 0:
        mod = n % base
        res.append(mod * power)
        num = num // base
        power *= base
    return res

        
def to_neg_base(n, base=-6):
    if n == 0:
        return "0"
    
    num = n
    
    digits = []
    power = 1
    remainders = []
    # Use standard decimal digits, adjust for larger bases if needed
    numerals = "0123456789abcdefghijklmnopqrstuvwxyz" 
    
    while n != 0:
        # Calculate remainder (modulo operation in Python can return negative)
        remainder = n % base
        # Calculate quotient using integer division
        n //= base


        # Adjust for negative remainder, as digits must be non-negative (0 to |base|-1)
        if remainder < 0:
            remainder += abs(base)
            n += 1

        remainders.append(remainder * power)
        num -= remainder * power
        # print(f"n {n}, num {num}, remainder {remainder}")
        power *= base
            
        digits.append(numerals[remainder])

    return remainders
    # The digits are collected in reverse order (least significant first)
    # return "".join(digits[::-1])

def to_neg_base_2(n, base=-6):
    if n == 0:
        return "0"
    
    num = n
    
    exp = 1
    remainders = []
    
    while num != 0:

        remainder = num % (base ** exp)

        if remainder != 0:
            remainder -= base ** exp
            # if exp % 2 == 1:
            #     remainder += abs(base ** exp)
            # else:
            #     remainder -= abs(base ** exp)

        num -= remainder
        
        remainders.append(remainder )
        # print(f"num {num}, remainder {remainder}")
        exp += 1

            

    # The digits are collected in reverse order (least significant first)
    print(f"Remainders: {remainders}")
    return remainders


for i in range(103, 160):
    print(f"Expansion of {i} in base 6: {to_neg_base(i)}")
    print(f"2 Expansion of {i} in base 6: {to_neg_base_2(i)}")
 
