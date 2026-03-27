LENGTH = 8
BORROW = "borrow"
CANNOT_BORROW = "cannot borrow"
def add_three_bits(a: str, b: str, c: int) -> (str, int):
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
            cpy = cpy[:i] + '01' + cpy[i+2:]
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
                return "subtraction result is negative"
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


# def division_helper(a: str, b: str) -> (str, str):
    

multiply_binary_strings("1011", "1101")

multiply_binary_strings("1011", "101")

