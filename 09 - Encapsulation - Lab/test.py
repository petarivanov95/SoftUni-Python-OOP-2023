# # Original Function
# def calculatetotal(val1, val2):
#     return val1 + val2
 
# def checkvalue(func):
    
#     # Inner Function to Validate Values
#     def wrapper(val1, val2):
#         if val1 >= 200 or val2 >= 200:
#             # Call the Original Function
#             return func(val1,val2)
#     # Return the final result
#     return wrapper
 
# cal = checkvalue(calculatetotal)
# total = cal(210, 10)
# print(total)


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '@' + last

    # def email(self):
    #     return '{}.{}@email.com'.format(self.first, self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')
emp_1.first = 'Hun'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())
