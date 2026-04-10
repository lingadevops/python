file_name = f"files.txt"
with open(file_name, "r") as file:
    lines = file.readlines()
    word_count = file.read().split()
    char_count = file.read().replace(" ", "")
    print(f"Number of lines: {len(lines)}")
    print(f"Number of words: {len(word_count)}")
    print(f"Number of characters: {len(char_count)}")
