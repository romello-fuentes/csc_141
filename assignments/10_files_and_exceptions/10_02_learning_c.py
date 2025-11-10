# 10-2, learning c, pg 229


path = 'C:/Users/romfu/Desktop/csc_141/assignments/10_files_and_exceptions/learning_python.txt.txt'

with open(path) as file:
    for line in file:
        modified_line = line.replace('Python', 'C')
        print(modified_line.strip())
