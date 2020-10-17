data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

for i in range(len(data)):
    j = i
    parent = (j - 1) // 2

    while (j > 0) and (data[parent] < data[j]):
        data[parent], data[j] = data[j], data[parent]
        j = parent
        parent = (j - 1) // 2

for i in range(len(data) - 1, 0, -1):
    data[i], data[0] = data[0], data[i]

    j = 0
    left = 2 * j + 1
    right = 2 * j + 2

    while ((left < i) and (data[j] < data[left])) \
            or ((right < i) and (data[j] < data[right])):

        if data[left] > data[right]:
            data[j], data[left] = data[left], data[j]
            j = left
        else:
            data[j], data[right] = data[right], data[j]
            j = right

        left = 2 * j + 1
        right = 2 * j + 2

print(data)
