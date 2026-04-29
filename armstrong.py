num = int(input("Enter a number: "))

length = len(str(num))
print(f"The number of digits in {num} is: {length}")

sum_of_powers = sum(int(digit) ** length for digit in str(num))
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")