n = 18

def convert(n, base):
    result = ''

    while n > 0:
        result = str(n % base) + result
        n //= base

    return result

def convert2(n):
    result = 0
    for i in range(len(n)):
        result += int(n[i]) * (2 ** (len(n) - 1 - i))
    return result

print(convert(n, 2))
print(convert(n, 3))
print(convert(n, 8))
print(convert(n, 10))

print(convert2('10010'))
