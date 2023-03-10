class PizzaDelivery:
    
    def __init__(self, name: str, price: float, ingredients: dict) -> None:
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False
    
    def add_extra(self, ingredient: str, quantity: float, price_per_quantity: float):
        if ingredient in self.ingredients.keys():
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity
        
        self.price += quantity*price_per_quantity
    
   
    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        
        if self.ingredients[ingredient] < quantity:
            return f"Please check again the desired quantity of {ingredient}!"
        
        self.ingredients[ingredient] -= quantity
        self.price -= price_per_quantity * quantity
    
    def make_order(self):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        
        self.ordered = True
        ingredients_str = ", ".join([f"{ingr}: {self.ingredients[ingr]}" for ingr in self.ingredients])
        return f"You've ordered pizza {self.name} prepared with {ingredients_str} and the price will be {self.price}lv."
