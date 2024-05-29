import json
from gate import Gate

def load_json(input_file):
    with open(input_file, 'r') as file:
        return json.load(file)

def initialize_gates(data):
    gate_list = []
    for entry in data:
        index = entry['index']
        name = entry['name']
        code = entry.get('sourceName', entry.get('sourceName ', '!NULL!'))
        cost = None
        gate_list.append(Gate(index, name, code))
    return gate_list

def process_data(data):
    return initialize_gates(data)
