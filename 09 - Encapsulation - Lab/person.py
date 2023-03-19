class Person:
    def __init__(self, age = 0):
        self.age = age

    @property
    def age(self):
        return f'Getting {self.__age}'

    @age.setter
    def age(self, age):
        if age < 18:
            self.__age = 18
            print("Setting Age for lower than 18")
        else:
            self.__age = age
            print("Setting age for greater or equal to 18")

person = Person(25)
print(person.age)