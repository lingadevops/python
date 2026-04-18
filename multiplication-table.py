number = int(input("Enter the number for which you want the multiplication table: "))
print(f"Multiplication Table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
