def hanoi(n, src, dest, via):
    if n > 1:
        hanoi(n - 1, src, via, dest)
        print(f'{src} -> {dest}')
        hanoi(n - 1, via, dest, src)
    else:
        print(f'{src} -> {dest}')

n = int(input())
hanoi(n, 'a', 'b', 'c')
