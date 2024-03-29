from project.meals.starter import Starter
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.client import Client


class FoodOrdersApp:
    INITIAL_RECEIPT_ID = 0
    VALID_MEALS = {
        "Starter": Starter,
        "Dessert": Dessert,
        "MainDish": MainDish
    }

    def __init__(self):
        self.menu = []
        self.clients_list = []

    @staticmethod
    def get_next_receipt_id():
        FoodOrdersApp.INITIAL_RECEIPT_ID += 1
        return FoodOrdersApp.INITIAL_RECEIPT_ID

    def get_client(self, phone_number):
        return next(filter(lambda x: (x for x in self.clients_list if x.phone_number == phone_number), self.clients_list))

    @staticmethod
    def check_client_shopping_cart(client):
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

    def register_client(self, client_phone_number):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                raise Exception("The client has already been registered!")

        client = Client(client_phone_number)
        self.clients_list.append(client)

        return f"Client {client_phone_number} registered successfully."

    def check_menu_ready(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if meal.__class__.__name__ in self.VALID_MEALS:
                self.menu.append(meal)

    def show_menu(self):
        self.check_menu_ready()
        return '\n'.join(str(meal.details()) for meal in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number, **meal_names_and_quantities):
        self.check_menu_ready()

        try:
            client = self.get_client(client_phone_number)
        except IndexError:
            self.register_client(client_phone_number)
            client = self.get_client(client_phone_number)

        meal_names = [m.name for m in self.menu]
        for meal_name, quantity in meal_names_and_quantities.items():
            if meal_name not in meal_names:
                raise Exception(f"{meal_name} is not on the menu!")

            current_meal = [m for m in self.menu if m.name == meal_name][0]
            if current_meal.quantity < quantity:
                client.shopping_cart = []

                raise Exception(f"Not enough quantity of {current_meal.__class__.__name__}: {meal_name}!")

            ordered_meal = self.VALID_MEALS[current_meal.__class__.__name__](meal_name, current_meal.price, quantity)
            client.shopping_cart.append(ordered_meal)

        for meal_name, quantity in meal_names_and_quantities.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity -= quantity

        client.bill = sum((m.quantity * m.price) for m in client.shopping_cart)

        return f"Client {client_phone_number} successfully ordered {', '.join(m.name for m in client.shopping_cart)} " \
               f"for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number):
        client = self.get_client(client_phone_number)

        self.check_client_shopping_cart(client)  # raises exception if shopping cart is empty

        for meal in self.menu:
            for order in client.shopping_cart:
                if order.name == meal.name:
                    meal.quantity += order.quantity

        client.shopping_cart = []
        client.bill = 0.0

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number):
        client = self.get_client(client_phone_number)
        self.check_client_shopping_cart(client)  # raises exception if shopping cart is empty

        receipt_id = self.get_next_receipt_id()
        total_paid_money = client.bill
        client.bill = 0
        client.shopping_cart = []

        return f"Receipt #{receipt_id} with total amount of {total_paid_money:.2f} " \
               f"was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

food_orders_app = FoodOrdersApp()
print(food_orders_app.register_client("0899999999"))

french_toast = Starter("French toast", 6.50, 5)
hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)

print(food_orders_app.add_meals_to_menu(
    french_toast, hummus_and_avocado_sandwich,
    tortilla_with_beef_and_pork,
    risotto_with_wild_mushrooms,
    chocolate_cake_with_mascarpone,
    chocolate_and_violets))
print(food_orders_app.show_menu())
food = {"Hummus and Avocado Sandwich": 5,
        "Risotto with Wild Mushrooms": 1,
        "Chocolate and Violets": 4}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))
additional_food = {"Risotto with Wild Mushrooms": 2,
                   "Tortilla with Beef and Pork": 2}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **additional_food))
print(food_orders_app.finish_order("0899999999"))
print(food_orders_app)

