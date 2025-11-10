# 10-3, learning python, pg 229


path = 'C:/Users/romfu/Desktop/csc_141/assignments/10_files_and_exceptions/learning_python.txt.txt'

with open(path) as file:
    for line in file.read().splitlines():
        print(line)
