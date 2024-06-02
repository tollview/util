import json
from models.gate import Gate
from models.ratedata import RateData
from models.locdata import LocData

def load_json(input_file):
    with open(input_file, 'r') as file:
        return json.load(file)

def initialize_gates(data):
    gate_list = []
    for entry in data:
        index = entry['index']
        name = entry['name']
        code = entry.get('sourceName', entry.get('sourceName ', entry.get('soruceName', entry.get('soruceName ', 'NULL'))))
        locx = entry['latitude']
        locy = entry['longitude']
        gate_list.append(Gate(index, name, code, locx, locy))
    return gate_list

def process_data(data):
    return initialize_gates(data)

def setup_ratedata(rates_data):
    rate_data_list = []
    for entry in rates_data['features']:
        plaza_id = entry['attributes']['PlazaID']
        code = entry['attributes']['PlazaCode']
        cost = entry['attributes']['TagFare']
        rate_data = RateData(plaza_id, code, cost)
        rate_data_list.append(rate_data)
    return rate_data_list

def setup_locdata(loc_data):
    loc_data_list = []
    for entry in loc_data['features']:
        plaza_id = entry['attributes']['PLAZA_ID']
        loc_name = entry['attributes']['ROADWAY_DESC']
        locx = entry['attributes']['X_COORD']
        locy = entry['attributes']['Y_COORD']
        loc_data = LocData(plaza_id, loc_name, locx, locy)
        loc_data_list.append(loc_data)
    return loc_data_list