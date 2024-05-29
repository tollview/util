class RateData:
    def __init__(self, plaza_id, code, cost):
        self.plaza_id = plaza_id
        self.code = code
        self.cost = cost

    def __repr__(self):
        return f"RateData(plaza_id={self.plaza_id}, code={self.code}, cost={self.cost})"