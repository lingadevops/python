num = int(input("Enter the number of terms: "))
a, b = 0, 1
count = 0

if num <= 0:
    print("Please enter a positive integer.")
elif num == 1:
    print("Fibonacci sequence up to", num, ":")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < num:
        print(a, end=' ')
        a, b = b, a + b
        count += 1