class Restaurant:

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        return "This is {} and we serve {} food.".format(self.name,self.cuisine)

    def open_restaurant(self):
        return f"{self.name}, a restaurant serving {self.cuisine} cuisine, is now open."

    def set_number_served(self, new_number_served):
        self.number_served = new_number_served

    def increment_number_served(self, increment_number_served):
        self.number_served += increment_number_served


restaurant_1 = Restaurant("Forlioni","Italian")
restaurant_2 = Restaurant("Minggs","Chinese")
restaurant_3 = Restaurant("Georgi","Bulgarian")

restaurant_1.set_number_served(5132)

print(restaurant_1.number_served)

restaurant_1.increment_number_served(5123123)

print(restaurant_1.number_served)
