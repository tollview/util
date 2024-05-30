from models.gate import Gate
from models.ratedata import RateData
from models.dbratematch import DbRateMatch

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