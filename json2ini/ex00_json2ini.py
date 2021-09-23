import json

with open("test.json") as json_file:
    json_data = json.load(json_file)

with open("fichier.ini", 'w') as fw:
    for key, value in json_data.items():
        fw.write(key + "=" + str(value) + "\n")