
from person import Person
class Employee(Person):
    def _init_(self, name, money, mood, healthRate, id, car, email, salary, distanceToWork):
        super()._init_(name, money, mood, healthRate)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self, distance):
        self.car.run(80, distance)

    def refuel(self, gasAmount=100):
        self.car.fuelRate += gasAmount

    def send_mail(self, to, subject, msg, receiver_name):
        with open("email.txt", "w") as f:
            f.write(f"From: {self.email}\n")
            f.write(f"To: {to}\n\n")
            f.write(f"Hi, {receiver_name}\n")
            f.write(f"{msg}\n\n")
            f.write(f"Subject: {subject}\n")