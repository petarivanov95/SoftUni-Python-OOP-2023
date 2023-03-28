import unittest


class Car:
    def __init__(self, name: str, model: str, engine: str):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"


car = Car("Kia", "Rio", "1.3L B3 I4")
print(car.get_info())

# class TestCar(unittest.TestCase):
#     def setUp(self) -> None:
#         self.car = Car("Kia", "Rio", "1.3L B3 I4")
#
#     def test_name_of_book(self):
#         result = self.car.name
#         self.assertEqual(result, 'Kia')
#
#     def test_model_car(self):
#         result = self.car.model
#         self.assertEqual(result, 'Rio')
#
#
# if __name__ == '__main__':
#     unittest.main()
