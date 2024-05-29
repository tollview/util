from models.gate import Gate
from models.ratedata import RateData
from models.dbratematch import DbRateMatch

def match_gates_and_rates(gates, rate_data_list):
    matched_data = []
    for gate in gates:
        for rate_data in rate_data_list:
            if gate.code == rate_data.code:
                match = DbRateMatch(gate.code, rate_data.cost)
                matched_data.append(match)
    return matched_data
