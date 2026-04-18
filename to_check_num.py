def to_check_num(num):
    if num < 0:
        print("Negative number")
    elif num == 0:
        print("Zero")
    else:
        print("Positive number")

number = float(input("Enter a number: "))
to_check_num(number)