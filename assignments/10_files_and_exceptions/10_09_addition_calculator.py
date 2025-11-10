# 10-9, silent cats and dogs, pg 238

filenames = ['C:/Users/romfu/Desktop/csc_141/assignments/10_files_and_exceptions/cats.txt', 'C:/Users/romfu/Desktop/csc_141/assignments/10_files_and_exceptions/dogs.txt']

for filename in filenames:
    try:
        with open(filename) as file:
            print(f"\nContents of {filename}:")
            print(file.read())
    except FileNotFoundError:
        pass  
