# Write a programe to create a dictionary of hindi words with values as their english translation. provide user with an option to look it up

words = {
    "Suraj": "Sun",
    "Sagar": "lake",
    "Roshni": "light",
    "Paisa": "Money",
    "Business": "Vyapar"
}
word = input("Enter the word you want meaning of: ")

#print(words[word])

# or 

print(words.get(word, "word not found"))












