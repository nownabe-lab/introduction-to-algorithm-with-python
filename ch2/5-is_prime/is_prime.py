import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# for i in range(200):
#     if is_prime(i):
#         print(i, end=' ')

def get_prime(n):
    if n <= 1:
        return []

    prime = [2]
    limit = int(math.sqrt(n))

    data = [i for i in range(3, n, 2)]
    while limit > data[0]:
        prime.append(data[0])
        data = [j for j in data if j % data[0] != 0]

    return prime + data

print(get_prime(200))
