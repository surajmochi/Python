# Extract only the alphabetic characters from the string(remove numbers).

text = "ComputerScience2026"

letters_only = ''.join([char for char in text if char.isalpha()])
print(letters_only)