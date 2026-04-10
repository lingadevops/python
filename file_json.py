import json

try:
    with open("config.json", "r") as file:
        config_data = json.load(file)
        for key, value in config_data.items():
            print(f"{key}: {value}")
except FileNotFoundError:
    print("The file 'config.json' was not found.")
except json.JSONDecodeError:
    print("Error decoding JSON from the file.")
