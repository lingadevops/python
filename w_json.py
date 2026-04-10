import json
data = input("Enter the name, namespace, status: ")
data_dict = {
    "name": data.split(",")[0],
    "namespace": data.split(",")[1],
    "status": data.split(",")[2]
}
with open("data.json", "w") as file:
    json.dump(data, file)

with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)