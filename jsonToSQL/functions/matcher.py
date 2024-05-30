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
        gate.name_less_direction = re.sub(r'\s[NSEW]\s', ' ', gate.name)
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