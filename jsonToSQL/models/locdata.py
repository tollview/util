class LocData:
    def __init__(self, plaza_id, loc_name, locx, locy):
        self.plaza_id = plaza_id
        self.loc_name = loc_name
        self.locx = locx
        self.locy = locy

    def __repr__(self):
        return f"LocData(plaza_id={self.plaza_id}, loc_name={self.loc_name}, locx={self.locx}, locy={self.locy})"