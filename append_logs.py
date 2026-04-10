from time import time

print(f"Start time: {time()}")

with open("logs.txt", "a") as f:
    f.write(f"Log entry at {time()}\n")

with open("logs.txt", "r") as f:
    print(f.read())