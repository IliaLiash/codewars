class Vector:

    def __init__(self, vector_1):
        self.vector_1 = vector_1

    def add(self, vector_2):
        res = []
        for i in range(len(self.vector_1)):
            res.append(self.vector_1[i] + vector_2.vector_1[i])
        return Vector(res)

    def subtract(self, vector_2):
        res = []
        for i in range(len(self.vector_1)):
            res.append(self.vector_1[i] - vector_2.vector_1[i])
        return Vector(res)

    def dot(self, vector_2):
        total = 0
        for i in range(len(self.vector_1)):
            total += self.vector_1[i] * vector_2.vector_1[i]
        return total

    def norm(self):
        total = 0
        for i in range(len(self.vector_1)):
            total += self.vector_1[i] ** 2
        return total ** 0.5
    
    #def equals(self, new_vector):
    #    return self.ve == new_vector
