letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
matrix = [[0,1], [2,3], [4,5], [6,7], [8,9], [10,11], [12,13], [14,15], [16,17], [18,19], [20,21], [22,23], [24,25]]

combined = letters + matrix
print(combined)

num= list(range(1, 11))
print(num)

nums = list(range(20))
print(nums)

print(len(nums))

#operations on list
print(letters[0]) #accessing first element
print(letters[1:5]) #accessing a range of elements
print(letters[-1]) #accessing last element
print(letters[-3:]) #accessing last three elements
print(letters[:5]) #accessing first five elements

letters[0] = "A" #modifying first element
print(letters)

for letter in letters:
    print(letter) #iterating through list

for letter in enumerate(letters):
    print(letter) #iterating with index


for index, letter in enumerate(letters):
    print(f"Index: {index}, Letter: {letter}") #iterating with index and value



#adding elements to list
letters.append("z") #adding element at the end
letters.insert(0, "A") #adding element at the beginning
print(letters)

#removing elements from list
letters.remove("A") #removing first occurrence of "A"
letters.pop() #removing last element
letters.pop(0) #removing first element
print(letters)

del letters[0] #deleting first element
del letters[0:3] #deleting a range of elements
print(letters)

letters.clear() #clearing the list
print(letters)


if "d" in letters:
    print("d is in the list")
else:    print("d is not in the list")

