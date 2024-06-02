from models.gate import Gate
from models.ratedata import RateData
from models.dbratematch import DbRateMatch
import re

def check_cardinality(gate_list):
    for gate in gate_list:
        if re.search(r'(\s)S(\s|$)', gate.name):
            gate.cardinality = "S"
        elif re.search(r'(\s)N(\s|$)', gate.name):
            gate.cardinality = "N"
        elif re.search(r'(\s)E(\s|$)', gate.name):
            gate.cardinality = "E"
        elif re.search(r'(\s)W(\s|$)', gate.name):
            gate.cardinality = "W"
        else:
            gate.cardinality = "-"
        gate.name_less_direction = re.sub(r'\s[NSEW](\s|$)', ' ', gate.name).strip()
    return gate_list

def pair_nswe_codes(gate_list):
    for gate in gate_list:
        gate.name_less_direction = gate.name_less_direction.replace(' Entry', '').replace(' Exit', '').strip()

    for i in range(len(gate_list) - 1):
        current_gate = gate_list[i]
        next_gate = gate_list[i + 1]

        if current_gate.name_less_direction == next_gate.name_less_direction:
            if current_gate.code == 'NULL' and next_gate.code != 'NULL':
                current_gate.code = next_gate.code
            elif next_gate.code == 'NULL' and current_gate.code != 'NULL':
                next_gate.code = current_gate.code

    return gate_list

def match_gates_and_rates(gates, rate_data_list):
    matched_data = []
    unmatched_data = []
    for rate_data in rate_data_list:
        matched = False
        for gate in gates:
            if gate.code == rate_data.code:
                match = DbRateMatch(gate.code, rate_data.cost, rate_data.plaza_id)
                matched_data.append(match)
                matched = True
                break
        if not matched:
            unmatched_data.append(rate_data)
    return matched_data, unmatched_data

def log_unmatched_data(unmatched_data):
    print("---rates mismatches---")
    for data in unmatched_data:
        print(f"{data.code} | {data.plaza_id}")