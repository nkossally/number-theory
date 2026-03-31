LENGTH = 8
BORROW = "borrow"
CANNOT_BORROW = "cannot borrow"
NEGATIVE_RESULT = "subtraction result is negative"
def add_three_bits(a: str, b: str, c: int) -> (str):
    one_count = 0
    if a == '1':
        one_count += 1
    if b == '1':
        one_count += 1
    if c == '1':
        one_count += 1
    if one_count == 0:
        return '00'
    if one_count == 1:
        return '01'
    if one_count == 2:
        return '10'
    if one_count == 3:        
        return '11'

def subtract_two_bits(a: str, b: str):
    if a == '0' and b == '0':
        return '0'
    if a == '0' and b == '1':
        return BORROW
    if a == '1' and b == '0':
        return '1'
    if a == '1' and b == '1':        
        return '0'

def add_binary_strings(a: str, b: str) -> str:
    a = a.zfill(LENGTH)
    b = b.zfill(LENGTH)
    carry = "0"
    result = ""

    for i in range(LENGTH - 1, -1, -1):

        sum = add_three_bits(a[i], b[i], carry)
        result += sum[1]
        carry = sum[0]



    result = result[::-1]
    return result

def handle_borrow(a: str, b: str, idx):
    cpy = a
    for i in range(idx- 1, -1, -1):
        if cpy[i] == '1':
            cpy = cpy[:i] + '0' + cpy[i+1:]
            cpy = cpy[:idx] + '1' + cpy[idx+1:]
            return cpy
        else:
            cpy = cpy[:i] + '1' + cpy[i+1:]
    return CANNOT_BORROW


def subtract_binary_strings(a: str, b: str) -> str:
    a = a.zfill(LENGTH)
    b = b.zfill(LENGTH)
    
    for i in range(LENGTH - 1, -1, -1):

        diff = subtract_two_bits(a[i], b[i])

        if diff == BORROW:
            a = handle_borrow(a, b, i)
            if a == CANNOT_BORROW:
                return NEGATIVE_RESULT
        else:
            a = a[:i] + diff + a[i+1:]
    
    return a


def multiply_binary_strings(a: str, b: str) -> str:
    a = a.zfill(LENGTH)
    b = b.zfill(LENGTH)
    result = "0" * LENGTH
    

    for i in range(len(b) - 1, -1, -1):
        tail = "0" * (len(b) - 1 - i)
        if b[i] == '1':
            transformed_a = (a + tail)[-LENGTH:]
            result = add_binary_strings(result, transformed_a)
            result = result[-LENGTH:]
    print(int(result, 2), result)
    return result


def division_helper(a: str, b: str) -> int:
    count = 0
    diff = subtract_binary_strings(a, b)
    while diff != NEGATIVE_RESULT:
        count += 1
        diff = subtract_binary_strings(diff, b)

    return count

def divide_binary_strings(a: str, b: str) -> (str):
    print(int(a, 2), a, int(b, 2), b)
    b = b.lstrip("0")
    res = ""
    remainder = a
    for i in range(LENGTH - 1, -1, -1):
        subtrahend = b + "0" * i
        if len(subtrahend) > LENGTH:
            res += "0"
            continue
        count = division_helper(remainder, subtrahend)
        if count:
            res += '1'
            remainder = subtract_binary_strings(remainder, subtrahend)
        else:
            res += '0'

    print(int(res, 2), res, "remainder", remainder)
    return res
        


    

divide_binary_strings("1111", "11")
divide_binary_strings("111101", "1101")
divide_binary_strings("1101101", "11101")
