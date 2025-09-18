def naturals_from(n):
    while True:
        yield n
        n = n+1

def is_a_multiple_of_any(i,numbers):
    for n in numbers:
        if i % n == 0:
            return True
    return False

assert not is_a_multiple_of_any(5,[2,3])
assert is_a_multiple_of_any(6,[2,3])

def primes():
    primes_so_far = []
    for i in naturals_from(2):
        if not is_a_multiple_of_any(i,primes_so_far):
            yield i
            primes_so_far.append(i)

# print(primes())



print(list(reversed([1,2,3,4])))
