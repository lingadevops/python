num = 100
while num > 0:
    print(num)
    num //= 2


command = ""
while command .lower() != "exit":
    command = input("Enter a command (type 'exit' to quit): ")
    print(f"You entered: {command}")
