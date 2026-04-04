def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")


greet("John", "Doe")

#perform the task
#return the result

def get_greeting(name):
    return f"Hello, {name}!"

greeting_message = get_greeting("Alice")
print(greeting_message)


#increment a number by given value
def increment(number, value):
    return number + value

result = increment(5, 3)
print(result)


#default parameter value

def increment(number, value=1):
    return number + value
result1 = increment(5)
result2 = increment(5, 2)
print(result1)  # Output: 6
print(result2)  # Output: 7


#xargs
def multiply(a, b):
    print(a * b)

multiply(4, 5)

def multiply(*numbers):
    print(numbers)
    total = 1
    for number in numbers:
        print(number)
        total *= number
    print(total)
    return total
        

value=multiply(4, 5)
print(value)


#xxargs
def print_info(**info):
    print(info)

print_info(name="Alice", age=30, city="New York")


#scope of variables

