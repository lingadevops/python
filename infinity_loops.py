while True:
    command = input("Enter a command (type 'exit' to quit): ")
    if command.lower() == "exit":
        print("Exiting the program. Goodbye!")
        break
    print(f"You entered: {command}")



count = 0
for num in range(1, 10):
    if num % 2 == 0:
        print(f"{num} is even.")
        count += 1

print(f"Total even numbers between 1 and 9: {count}")
        
