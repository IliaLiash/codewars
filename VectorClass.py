class Vector:
    
    def __init__(self, vector):
        self.vector = vector
        
    def __str__(self):
        s = str(self.vector).replace('[','(').replace(']',')').replace(' ','')
        return s

    def add(self, vector_2):
        res = []
        for i in range(len(self.vector)):
            res.append(self.vector[i] + vector_2.vector[i])
        return Vector(res)

    def subtract(self, vector_2):
        res = []
        for i in range(len(self.vector)):
            res.append(self.vector[i] - vector_2.vector[i])
        return Vector(res)

    def dot(self, vector_2):
        total = 0
        for i in range(len(self.vector)):
            total += self.vector[i] * vector_2.vector[i]
        return total

    def norm(self):
        total = 0
        for i in range(len(self.vector)):
            total += self.vector[i] ** 2
        return total ** 0.5
    
    def equals(self, vector_2):
        if self.vector == vector_2.vector:
            return True
        return False
