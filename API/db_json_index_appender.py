import json
input_file = './API/json/dbsnapshot.json'

with open(input_file, 'r') as file:
    data = json.load(file)
for index, entry in enumerate(data):
    entry['index'] = index
with open(input_file, 'w') as file:
    json.dump(data, file, indent=4)

print(f"dbsnapshot annotated with indices")