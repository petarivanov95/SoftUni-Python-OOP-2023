class Employee:
    MONTHS = 12

    def __init__(self, employee_id: int, first_name: str, last_name: str, salary: int):
        """
        Constructor for Employee class.
        :param employee_id: The ID of the employee.
        :param first_name: The first name of the employee.
        :param last_name: The last name of the employee.
        :param salary: The salary of the employee.
        """
        self.id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self) -> str:
        """
        Returns the full name of the employee.
        :return: A string representing the full name of the employee.
        """
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self) -> int:
        """
        Returns the annual salary of the employee.
        :return: An integer representing the annual salary of the employee.
        """
        return self.salary * self.MONTHS

    def raise_salary(self, amount: int) -> int:
        """
        Increases the salary of the employee by a given amount.
        :param amount: The amount to increase the salary by.
        :return: An integer representing the new salary of the employee.
        """
        self.salary += amount

        return self.salary


employee = Employee(744423129, "John", "Smith", 1000) # creates an Employee object with ID 744423129, first name "John", last name "Smith", and salary 1000
print(employee.get_full_name()) # prints the full name of the employee
print(employee.raise_salary(500)) # increases the salary of the employee by 500 and prints the new salary
print(employee.get_annual_salary()) # prints the annual salary of the employee
