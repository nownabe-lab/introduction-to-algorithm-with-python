import os

queue = ['/home/nownabe/src/github.com/nownabe-lab/introduction-to-algorithm-with-python/']

while len(queue) > 0:
    dir = queue.pop()
    for i in os.listdir(dir):
        if i == 'search_file2.py':
            print(dir + i)
        if os.path.isdir(dir + i):
            if os.access(dir + i, os.R_OK):
                queue.append(f'{dir}{i}/')
