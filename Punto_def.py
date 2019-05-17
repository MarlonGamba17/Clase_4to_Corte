class punto_cordenada:

    X = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'punto en x {self.x} and y es {self.y}'


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def desplazar_x(self, other):
        return  self.x == other.x

    def desplazar_y(self, other):
        return  self.y == other.y

    def hallar_pendiente(self, other):
        return  self.x == other.x and self.y == other.y

    def distancia(self, other):
        distancia = ((other.x-self.x)**2)+((other.y - self.y)**2)
        return  distancia