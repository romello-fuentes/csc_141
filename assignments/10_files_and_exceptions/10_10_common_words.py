# 10-10, common words, pg 238

filename = 'C:/Users/romfu/Desktop/csc_141/assignments/10_files_and_exceptions/gutenberg_text.txt'  # Replace with your actual file name

try:
    with open(filename, encoding='utf-8') as file:
        text = file.read().lower()
        count_the = text.count('the')
        count_the_space = text.count('the ')
        print(f"'the' appears {count_the} times (approximate).")
        print(f"'the ' appears {count_the_space} times (more accurate).")
except FileNotFoundError:
    print("Text file not found. Please check the filename.")
