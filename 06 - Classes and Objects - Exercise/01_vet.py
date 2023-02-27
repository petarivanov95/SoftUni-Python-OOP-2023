class Vet:
    SPACE = 5
    ANIMALS = []
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.animals = []

    def register_animal(self, animal_name) -> str:
        if len(Vet.ANIMALS) < Vet.SPACE:
            Vet.ANIMALS.append(animal_name)
            self.animals.append(animal_name)
            return f"{animal_name} registered in the clinic"
        else:
            return "Not enough space"

    def unregister_animal(self, animal_name):
        if animal_name in Vet.ANIMALS:
            self.animals.remove(animal_name)
            Vet.ANIMALS.remove(animal_name)
            return f"{animal_name} unregistered successfully"
        else:
            return f"{animal_name} not in the clinic" 
    
    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.SPACE-len(Vet.ANIMALS)} space left in clinic"

peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())