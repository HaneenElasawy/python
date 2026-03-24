from  Person import Person
from car import Car
from employee import Employee
from office import Office


p1 = Person("Samy", 5000, "happy", 100)
print(p1.name, p1.money, p1.mood, p1.healthRate)

p1.sleep(5)
print("Mood after sleep:", p1.mood)

p1.eat(2)
print("Health after eating:", p1.healthRate)

p1.buy(3)
print("Money after buying:", p1.money)


car1 = Car("Fiat 128", 100, 60)
print(car1.name, car1.fuelRate, car1.velocity)

car1.run(80, 50)
print("Fuel after run:", car1.fuelRate)
print("Velocity after stop:", car1.velocity)


car2 = Car("Fiat 128", 100, 60)
emp1 = Employee("Samy", 5000, "happy", 100, 1, car2, "samy@mail.com", 5000, 20)

print(emp1.name, emp1.id, emp1.email, emp1.salary, emp1.distanceToWork)

emp1.work(9)
print("Mood after work:", emp1.mood)

emp1.drive(30)
print("Fuel after driving:", emp1.car.fuelRate)
print("Velocity after driving:", emp1.car.velocity)

emp1.refuel(50)
print("Fuel after refuel:", emp1.car.fuelRate)

emp1.send_mail("to@mail.com", "Email Subject", "This is an email template", "Mohamed")


office1 = Office("ITI")

car3 = Car("Fiat 128", 100, 60)
car4 = Car("BMW", 80, 100)

emp2 = Employee("Samy", 5000, "happy", 100, 1, car3, "samy@mail.com", 5000, 20)
emp3 = Employee("Ali", 3000, "tired", 75, 2, car4, "ali@mail.com", 6000, 15)

office1.hire(emp2)
office1.hire(emp3)

print("All Employees:")
for emp in office1.get_all_employees():
    print(emp.name, emp.id)

emp = office1.get_employee(1)
if emp:
    print(emp.name, emp.salary)

office1.reward(1, 500)
print("Salary after reward:", office1.get_employee(1).salary)

office1.deduct(2, 200)
print("Salary after deduction:", office1.get_employee(2).salary)

office1.check_lateness(1, 8.5)
office1.check_lateness(2, 8.0)

print("Employees number:", Office.employeesNum)

office1.fire(2)
print("Employees after fire:")
for emp in office1.get_all_employees():
    print(emp.name, emp.id)

print("Employees number after fire:", Office.employeesNum)

office1.save_to_json()
print("Office data saved to office.json")