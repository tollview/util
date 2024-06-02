class RateData:
    def __init__(self, plaza_id, code, cost, loc_name=None, locx=None, locy=None):
        self.plaza_id = plaza_id
        self.code = code
        self.cost = cost
        self.loc_name = loc_name
        self.locx = locx
        self.locy = locy

    def __repr__(self):
        return f"RateData(plaza_id={self.plaza_id}, code={self.code}, cost={self.cost}, loc_name={self.loc_name}, locx={self.locx}, locy={self.locy})"