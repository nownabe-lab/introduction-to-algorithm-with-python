import os

def search(dir, name):
    for i in os.listdir(dir):
        if i == name:
            print(dir + i)
        if os.path.isdir(dir + i):
            if os.access(dir + i, os.R_OK):
                search(f'{dir}{i}/', name)

search('/home/nownabe/src/github.com/nownabe-lab/introduction-to-algorithm-with-python/', 'search_file1.py')
