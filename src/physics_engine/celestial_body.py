from physics_engine.vector import Vector


class CelestialBody:
    def __init__(self, x, y, mass, radius, velocity_x=0, velocity_y=0):
        self.position = Vector(x, y)
        self.velocity = Vector(velocity_x, velocity_y)
        self.acceleration = Vector(0, 0)
        self.mass = mass
        self.radius = radius

    def get_position(self):
        return self.position.get_vector()

    def get_velocity(self):
        return self.velocity.get_vector()

    def get_acceleration(self):
        return self.acceleration.get_vector()

    def get_mass(self):
        return self.mass

    def get_radius(self):
        return self.radius

    #Updates position of body using suvat formula for x and for y
    #new_x = old_x + vx * dt + 0.5 * ax * dt^2 
    def update_position(self, dt):
        displacement = (self.velocity.multiply(dt)).add(self.acceleration.multiply(0.5*dt*dt))
        self.position = self.position.add(displacement)

    #Updates velocity using an average of initial acceleration in the frame and final acceleration
    #new_v = old_v + 0.5 * (old_a + new_a) * dt
    def update_velocity(self, new_acceleration, dt):
        average_acceleration = (self.acceleration.add(new_acceleration)).multiply(0.5)
        self.velocity = self.velocity.add(average_acceleration.multiply(dt))
        self.acceleration = new_acceleration      #

    
