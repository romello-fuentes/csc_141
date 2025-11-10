# 10-1, learning python, pg 228


path = 'C:/Users/romfu/Desktop/csc_141/assignments/10_files_and_exceptions/learning_python.txt.txt'

# Print entire file contents
with open(path) as file:
    contents = file.read()
    print("Full file contents:\n")
    print(contents)

# Print each line from the file
print("\nLine-by-line output:\n")
with open(path) as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
