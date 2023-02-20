class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

emp1 = Employee('Petar','Ivanov',500000)

print(emp1.fullname())

