import math

#Creates the class for a vector taking in the x and the y coordinates
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #get_vector is just a getter method to return a copy of the vector
    def get_vector(self):
        return (self.x, self.y)

    #add method takes another vector and adds them together creating new vector
    def add(self, other_vector):
        other_vector = other_vector.get_vector()
        new_vector = Vector(self.x + other_vector[0], self.y + other_vector[1])
        return new_vector

    #subtract method takes a different vector and subtracts them from each other giving a vector between the 2
    def subtract(self, other_vector):
        other_vector = other_vector.get_vector()
        new_vector = Vector(self.x - other_vector[0], self.y - other_vector[1])
        return new_vector

    #multiply takes a multiplier value and multiplies the vector by it creating new vector
    def multiply(self, multiplier):
        new_vector = Vector(self.x * multiplier, self.y * multiplier)
        return new_vector

    #calculates the magnitude of the vector
    #calculates the distance bewteen 2 bodies when there is a vector between them
    def magnitude(self):
        distance = math.sqrt(self.x**2 + self.y**2)
        return distance

    #normalises the vector meaning it is scaled to one unit
    def normalise(self):
        magnitude = self.magnitude()
        if magnitude == 0:          #Checks that magnitude is not 0 to avoid error when dividing by 0
            return Vector(0,0)
        new_x, new_y = self.x / magnitude, self.y / magnitude  #Dividing by magnitude scales the vector down to 1
        return Vector(new_x, new_y)

