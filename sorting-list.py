numbers = [5, 2, 9, 1, 5, 6]

numbers.sort() #sorts the list in ascending order
print(numbers)
numbers.sort(reverse=True) #sorts the list in descending order
print(numbers)
print(sorted(numbers)) #returns a new sorted list without modifying the original
print(sorted(numbers, reverse=True)) #returns a new sorted list in descending order without modifying the original


items = ["banana", "apple", "cherry", "date"]
items.sort() #sorts the list in alphabetical order
print(items)

items = [
    ("banana", 3),
    ("apple", 2),
    ("cherry", 5),
    ("date", 1)
]

def sort_by_name(item):
    return item[1]

items.sort(key=sort_by_name) #sorts the list of tuples based on the second element (quantity)
print(items)


#lambda function for sorting
items.sort(key=lambda item: item[1]) #sorts the list of tuples based on the second element (quantity) using a lambda function
print(items)

#map function

#without map

items = [
    ("banana", 3),
    ("apple", 2),
    ("cherry", 5),
    ("date", 1)
]

prices = []
for item in items:
    price = item[1]
    prices.append(price)
print(prices)

#with map

prices = list(map(lambda item: item[1], items)) #using map to extract the second element (quantity) from each tuple
print(prices)


#filter function
x=list(filter(lambda item: item[1] > 2, items)) #using filter to get items with quantity greater than 2
print(x)


#list comprehension

#[expression for item in items]
prices = [item[1] for item in items]
print(prices)

filtered_items = [item for item in items if item[1] > 2] #using list comprehension to filter items with quantity greater than 2
print(filtered_items)


#stack
#LIFO - Last In First Out
#pop

#queue
#FIFO - First In First Out

#array
from array import array
numbers =  array("i", [1, 2, 3, 4, 5]) #creating an array of integers
print(numbers)

#set

num = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
unique_num = set(num) #creating a set from the list to get unique elements
print(unique_num)

num2 = [1, 2, 3, 4, 5, 11, 12, 15, 16, 17, 18, 19, 20]
print(set(num) & set(num2)) #intersection of two sets
print(set(num) | set(num2)) #union of two sets
print(set(num) - set(num2)) #difference of two sets 


#dictionary
point = {"x": 1, "y": 2} #creating a dictionary with keys "x" and "y"
print(point)

point = dict(x=1, y=2) #creating a dictionary using the dict constructor
print(point)

values = []
for x in range(5):
    values.append(x * 2) #using a loop to create a list of values
print(values)

values = [x * 2 for x in range(5)] #using list comprehension to create a list of values
print(values)

values = {x * 2 for x in range(5)} #using set comprehension to create a set of values
print(values)


values = {x:x * 2 for x in range(5)} #using Dict comprehension to create a set of values
print(values)


#generators

from sys import getsizeof
values = [x * 2 for x in range(1000)] #using list comprehension to create a list of values
print(getsizeof(values)) #getting the size of the list in bytes

values = (x * 2 for x in range(1000)) #using generator expression to create a generator of values
print(getsizeof(values)) #getting the size of the generator in bytes