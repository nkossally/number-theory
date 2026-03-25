LENGTH = 8
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
        return None
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
    print(result, int(result, 2))
    return result

def subtract_binary_strings(a: str, b: str) -> str:
    a = a.zfill(LENGTH)
    b = b.zfill(LENGTH)
    result = ""

    for i in range(LENGTH - 1, -1, -1):

        diff = subtract_two_bits(a[i], b[i])
        if diff == None:
            return None
        result += diff
    
    result = result[::-1]
    print(result, int(result, 2))
    return result

def subtract_binary_strings(a: str, b: str) -> str:
    a = a.zfill(LENGTH)
    b = b.zfill(LENGTH)
   

def multiply_binary_strings(a: str, b: str) -> str:
    a = a.zfill(LENGTH)
    b = b.zfill(LENGTH)
    result = "0" * LENGTH



    print(result, int(result, 2))
    return result

add_binary_strings("1010", "1101")
add_binary_strings("1111", "1111")
