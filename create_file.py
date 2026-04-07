server_name = str(input("Enter the 5 server names (comma-separated): "))
file_name = f"server_name.txt"
for server in server_name.split(","):
    print(server.strip())
    with open(file_name, "a") as file:
        file.write(f"Server Name: {server.strip()}\n")

print(f"Server names have been written to {file_name}")


with open(file_name, "r") as file:
     print(file.read())