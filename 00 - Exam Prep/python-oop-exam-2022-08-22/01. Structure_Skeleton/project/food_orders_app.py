from project.meals.starter import Starter
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.client import Client


class FoodOrdersApp:
    VALID_MEALS = {'Starter': Starter, 'Dessert': Dessert,'Main Dish': MainDish}

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number:str):
        for client in self.clients_list:
            if client_phone_number == client.phone_number:
                raise Exception("The client has already been registered!")

        client = Client(client_phone_number)
        self.clients_list.append(client)

    def 




food_orders_app = FoodOrdersApp()
