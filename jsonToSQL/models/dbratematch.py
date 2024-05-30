class DbRateMatch:
    def __init__(self, code, cost, plaza_id):
        self.code = code
        self.cost = cost
        self.plaza_id = plaza_id

    def __repr__(self):
        return f"DbRateMatch(code={self.code}, cost={self.cost}, plaza_id={self.plaza_id})"
