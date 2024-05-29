import json
from gate import Gate

def load_json(input_file):
    with open(input_file, 'r') as file:
        return json.load(file)

def process_data(data):
    gate_list = []
    for entry in data:
        index = entry['index']
        name = entry['name']
        code = entry.get('sourceName', entry.get('sourceName ', '!NULL!'))
        gate_list.append(Gate(index, name, code))
    return gate_list
