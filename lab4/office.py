import json


class Office:
    employeesNum = 0

    def _init_(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for emp in self.employees:
            if emp.id == empId:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, empId):
        for emp in self.employees:
            if emp.id == empId:
                self.employees.remove(emp)
                Office.employeesNum -= 1
                break

    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp is not None:
            emp.salary -= deduction

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp is not None:
            emp.salary += reward

    def check_lateness(self, empId, moveHour):
        emp = self.get_employee(empId)
        if emp is not None:
            is_late = Office.calculate_lateness(9, moveHour, emp.distanceToWork, emp.car.velocity)
            if is_late:
                self.deduct(empId, 10)
                print(f"{emp.name} is late")
            else:
                self.reward(empId, 10)
                print(f"{emp.name} is on time")

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        if velocity == 0:
            return True

        arrival_time = moveHour + (distance / velocity)
        return arrival_time > targetHour

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num

    def to_dict(self):
        return {
            "office_name": self.name,
            "employeesNum": Office.employeesNum,
            "employees": [
                {
                    "id": emp.id,
                    "name": emp.name,
                    "money": emp.money,
                    "mood": emp.mood,
                    "healthRate": emp.healthRate,
                    "email": emp.email,
                    "salary": emp.salary,
                    "distanceToWork": emp.distanceToWork,
                    "car": {
                        "name": emp.car.name,
                        "fuelRate": emp.car.fuelRate,
                        "velocity": emp.car.velocity
                    }
                }
                for emp in self.employees
            ]
        }

    def save_to_json(self, filename="office.json"):
        with open(filename, "w") as f:
            json.dump(self.to_dict(), f, indent=4)