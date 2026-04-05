#most repeated char in sentence
sentence = "This is a common interview question"

sentence = sentence.replace(' ', '')

#values = [char for char in sentence]
#print(values)

values = {char: sentence.count(char) for char in sentence} #using dict comprehension to create a dictionary with characters as keys and their counts as values
values1 = (sorted(values.items(), key=lambda x: x[1]))

print(values1[-1]) #printing the character with the highest count
#repeated_char = [char for char in sentence if sentence.count(char) >= 5] #using list comprehension to create a list of characters that are repeated
#print(repeated_char)
