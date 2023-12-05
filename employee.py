"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract_type, salary=0, hours_worked=0, hourly_rate=0, bonus=0, contracts_landed=0, commission_rate=0):
        self.name = name
        self.contract_type = contract_type
        self.salary = salary
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.bonus = bonus
        self.contracts_landed = contracts_landed
        self.commission_rate = commission_rate

    def get_pay(self):
        if self.contract_type == "salary" and self.bonus == 0 and self.contracts_landed == 0:
            return self.salary
        elif self.contract_type == "hourly" and self.bonus == 0 and self.contracts_landed == 0:
            return self.hours_worked * self.hourly_rate
        elif self.contract_type == "salary" and self.bonus > 0 and self.contracts_landed == 0:
            return self.salary + self.bonus
        elif self.contract_type == "hourly" and self.bonus > 0 and self.contracts_landed == 0:
            return self.hours_worked * self.hourly_rate + self.bonus
        elif self.contract_type == "salary" and self.bonus == 0 and self.contracts_landed > 0:
            return self.salary + self.contracts_landed * self.commission_rate
        elif self.contract_type == "hourly" and self.bonus == 0 and self.contracts_landed > 0:
            return self.hours_worked * self.hourly_rate + self.contracts_landed * self.commission_rate

    def __str__(self):
        if self.contract_type == "salary" and self.bonus == 0 and self.contracts_landed == 0:
            return f"{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}."
        elif self.contract_type == "hourly" and self.bonus == 0 and self.contracts_landed == 0:
            return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour. Their total pay is {self.get_pay()}."
        elif self.contract_type == "salary" and self.bonus > 0 and self.contracts_landed == 0:
            return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."
        elif self.contract_type == "hourly" and self.bonus > 0 and self.contracts_landed == 0:
            return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."
        elif self.contract_type == "salary" and self.bonus == 0 and self.contracts_landed > 0:
            return f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.contracts_landed} contract(s) at {self.commission_rate}/contract. Their total pay is {self.get_pay()}."
        elif self.contract_type == "hourly" and self.bonus == 0 and self.contracts_landed > 0:
            return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour and receives a commission for {self.contracts_landed} contract(s) at {self.commission_rate}/contract. Their total pay is {self.get_pay()}."

# Test Cases
billie = Employee("Billie","salary", salary=4000)
charlie = Employee("Charlie","hourly", hours_worked=100, hourly_rate=25)
renee = Employee("Renee","salary", salary=3000, contracts_landed=4, commission_rate=200)
jan = Employee("Jan","hourly", hours_worked=150, hourly_rate=25, contracts_landed=3, commission_rate=220)
robbie = Employee("Robbie","salary", salary=2000, bonus=1500)
ariel = Employee("Ariel","hourly", hours_worked=120, hourly_rate=30, bonus=600)

print(billie.get_pay())  # Should return 4000
print(str(billie))  # Should print "Billie works on a monthly salary of 4000. Their total pay is 4000."

print(charlie.get_pay())  # Should return 2500
print(str(charlie))  # Should print "Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500."

print(renee.get_pay())  # Should return 3800
print(str(renee))  # Should print "Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800."

print(jan.get_pay())  # Should return 4410
print(str(jan))  # Should print "Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410."

print(robbie.get_pay())  # Should return 3500
print(str(robbie))  # Should print "Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500."

print(ariel.get_pay())  # Should return 4200
print(str(ariel))  # Should print "Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200."

