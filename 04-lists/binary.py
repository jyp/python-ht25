
# example:
# 35 --> 1
# 34
# 17  -> 1
# ...

def to_binary_string(n):
    if n == 0: return "0" # special case!
    result = ""
    while n > 0:
        last_bit = n % 2
        result = str(last_bit) + result
        n = n // 2
    return result

def from_binary_string(s):
    result = 0
    for bit in s:
        result = result * 2 + int(bit)
    return result

# print(to_binary_string(35))
print(from_binary_string(""))
print(to_binary_string(0))
