class Shop:
    def __init__(self, name: str, items: list):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)


lidl = Shop("Lidl", ["Apples", "Bananas", "Cucumbers"]) # creates a Shop object named "Lidl" with 3 items
bila = Shop("Bila", ["Oranges", "Grapes", "Tomatoes"]) # creates a Shop object named "Bila" with 3 different items

print(lidl.get_items_count())
