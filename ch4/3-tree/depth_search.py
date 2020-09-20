tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12],
        [13, 14], [], [], [], [], [], [], [], []]

def search(pos):
    print(pos, end=' ')
    for i in tree[pos]:
        search(i)

def search2(pos):
    for i in tree[pos]:
        search2(i)
    print(pos, end=' ')

def search3(pos):
    if len(tree[pos]) == 2:
        search3(tree[pos][0])
        print(pos, end=' ')
        search3(tree[pos][1])
    elif len(tree[pos]) == 1:
        search3(tree[pos][0])
        print(pos, end=' ')
    else:
        print(pos, end=' ')

search3(0)
