class Casa:

    banos = 0
    ambientes = 0

    def __init__(self, direccion):
        self.direccion = direccion
        self.ambientes = 0
        self.banos = 0

    def __repr__(self):
        return f'Casa ubicada en {self.direccion}'

    def __eq__(self, other):
        return self.banos == other.banos and self.ambientes == other.ambientes
