MAX_FLOOR = 10

patterns = [0]

for i in range(MAX_FLOOR-1):
    f = MAX_FLOOR - i - 1
    pattern = sum(patterns) + 1
    patterns.append(pattern)
    print(f'{f} -> {MAX_FLOOR}: {pattern}')

# 2^(n-2)
