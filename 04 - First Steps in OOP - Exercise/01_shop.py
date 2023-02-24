class Shop:
    def __init__(self, name, items):
        """
        Constructor for Shop class.
        :param name: The name of the shop.
        :param items: A list of items sold in the shop.
        """
        self.name = name
        self.items = items

    def get_items_count(self):
        """
        Returns the number of items sold in the shop.
        :return: The number of items sold in the shop.
        """
        return len(self.items)


lidl = Shop("Lidl", ["Apples", "Bananas", "Cucumbers"]) # creates a Shop object named "Lidl" with 3 items
bila = Shop("Bila", ["Oranges", "Grapes", "Tomatoes"]) # creates a Shop object named "Bila" with 3 different items
