def bin_sort(data):
    bucket = []
    for d in data:
        if len(bucket) <= d:
            bucket += [0] * (d - len(bucket) + 1)
        bucket[d] += 1

    result = []
    for i, c in enumerate(bucket):
        for _ in range(c):
            result.append(i)
    return result

data = [9, 4, 5, 2, 8, 3, 7, 8, 3, 2, 6, 5, 7, 9, 2, 9]

print(bin_sort(data))
