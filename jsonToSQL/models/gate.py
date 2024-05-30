class Gate:
    def __init__(self, index, name, code, locx, locy, cardinality=None, name_less_direction=None):
        self.index = index
        self.name = name
        self.code = code
        self.locx = locx
        self.locy = locy
        self.cardinality = cardinality
        self.name_less_direction = name_less_direction

    def __repr__(self):
        return f"Gate(index={self.index}, name={self.name}, code={self.code}, locx={self.locx}, locy={self.locy}, cardinality={self.cardinality}, name_less_direction={self.name_less_direction})"
