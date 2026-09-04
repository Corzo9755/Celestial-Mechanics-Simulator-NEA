import math
from physics_engine.vector import Vector

G = 6.674e-11 
#gravitational constant
G = 1  # scaled up for simulation purposes


class Simulation:
    def __init__(self):
        self.bodies = []

    def calculate_force(self, body_a, body_b):
        #Returns the force vector pulling body_a toward body_b
        direction = body_b.position.subtract(body_a.position)
        distance = direction.magnitude()

        if distance == 0:
            return Vector(0, 0)  #avoid divide-by-zero, skip this pair collision

        force_magnitude = (G * body_a.mass * body_b.mass) / (distance ** 2)
        unit_direction = direction.normalise()
        force = unit_direction.multiply(force_magnitude)
        return force

    def step(self, dt):
        #Calculate new acceleration for every body, based on current positions
        new_accelerations = []
        for body in self.bodies:
            total_force = Vector(0, 0)
            for other in self.bodies:
                if other is not body:
                    total_force = total_force.add(self.calculate_force(body, other))
            acceleration = total_force.multiply(1 / body.mass)  # F = ma, so a = F/m
            new_accelerations.append(acceleration)

        #Update every body's position using its CURRENT (old) acceleration
        for body in self.bodies:
            body.update_position(dt)

        #Recalculate acceleration at the NEW positions
        newer_accelerations = []
        for body in self.bodies:
            total_force = Vector(0, 0)
            for other in self.bodies:
                if other is not body:
                    total_force = total_force.add(self.calculate_force(body, other))
            acceleration = total_force.multiply(1 / body.mass)
            newer_accelerations.append(acceleration)

        #Update velocity for every body using the average of old and new acceleration
        for body, new_acc in zip(self.bodies, newer_accelerations):
            body.update_velocity(new_acc, dt)