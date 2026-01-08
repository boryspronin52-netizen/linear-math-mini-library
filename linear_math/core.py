from math import sqrt

class Vector:

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):

        self.x = x
        self.y = y
        self.z = z

    @property
    def xyz(self):

        return [self.x, self.y, self.z]

    @property
    def length(self):

        return sqrt(self.x**2 + self.y**2 + self.z**2)

    @property
    def normalized(self):

        m = max(self.x, self.y, self.z)
        return [self.x / m, self.y / m, self.z / m]

    def __add__(self, other):

        if type(other) == Vector:
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

        elif type(other) == float:
            return Vector(self.x + other, self.y + other, self.z + other)

        else:
            raise ValueError("Unsupported operand type(s) for +")

    def __sub__(self, other):

        if type(other) == Vector:
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

        elif type(other) == float:
            return Vector(self.x - other, self.y - other, self.z - other)

        else:
            raise ValueError("Unsupported operand type(s) for -")

    def __mul__(self, other):

        if type(other) == Vector:
            return Vector(self.x * other.x, self.y * other.y, self.z * other.z)

        elif type(other) == float:
            return Vector(self.x * other, self.y * other, self.z * other)

        else:
            raise ValueError("Unsupported operand type(s) for *")

    def __truediv__(self, other):

        if type(other) == Vector:
            return Vector(self.x / other.x, self.y / other.y, self.z / other.z)

        elif type(other) == float:
            return Vector(self.x / other, self.y / other, self.z / other)

        else:
            raise ValueError("Unsupported operand type(s) for /")

    def dot(self, other):

        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def normalize(self):

        m = max(self.x, self.y, self.z)
        self.x, self.y, self.z = self.x / m, self.y / m, self.z / m

class Matrix:

    def __init__(self, data: list):

        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other):

        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have same size")

        result = [[self.data[r][c] + other.data[r][c] for c in range(self.cols)] for r in range(self.rows)]
        return result

    def __sub__(self, other):

        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have same size")

        result = [[self.data[r][c] + other.data[r][c] for c in range(self.cols)] for r in range(self.rows)]
        return result

    def __mul__(self, other):

        if isinstance(other, (int, float)):
            result = [[self.data[r][c] * other for r in range(self.rows)] for c in range(self.cols)]

        elif isinstance(other, Matrix) and (self.rows != other.rows or self.cols != other.cols):
            result = [[self.data[r][c] * other.data[r][c] for c in range(self.cols)] for r in range(self.rows)]

        else:
            raise ValueError("Unsupported operand type(s) for *")

        return result