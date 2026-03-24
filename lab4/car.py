

class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    def run(self, velocity, distance):
        self.velocity = velocity

        while distance > 0 and self.fuelRate > 0:
            distance -= 10
            self.fuelRate -= 10

        self.stop(distance)

    def stop(self, remaining_distance=0):
        self.velocity = 0
        if remaining_distance <= 0:
            print("You arrived safely")
        else:
            print(f"You stopped. Remaining distance: {remaining_distance}")