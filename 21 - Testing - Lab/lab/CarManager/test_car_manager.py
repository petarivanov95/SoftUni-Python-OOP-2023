import unittest
from car_manager import Car


class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car("Toyota", "Camry", 7.5, 60)

    def test_constructor(self):
        self.assertEqual(self.car.make, "Toyota")
        self.assertEqual(self.car.model, "Camry")
        self.assertEqual(self.car.fuel_consumption, 7.5)
        self.assertEqual(self.car.fuel_capacity, 60)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_make_validation(self):
        with self.assertRaises(Exception) as context:
            self.car.make = ""
        self.assertEqual(str(context.exception), "Make cannot be null or empty!")

    def test_model_validation(self):
        with self.assertRaises(Exception) as context:
            self.car.model = ""
        self.assertEqual(str(context.exception), "Model cannot be null or empty!")

    def test_fuel_consumption_validation(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = -7.5
        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_validation(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = -60
        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount_validation(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -10
        self.assertEqual(str(context.exception), "Fuel amount cannot be negative!")

    def test_refuel(self):
        self.car.refuel(20)
        self.assertEqual(self.car.fuel_amount, 20)
        self.car.refuel(50)
        self.assertEqual(self.car.fuel_amount, 60)

    def test_refuel_validation(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(-10)
        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")

    def test_drive(self):
        self.car.refuel(20)
        self.car.drive(200)
        self.assertEqual(self.car.fuel_amount, 5)

    def test_drive_validation(self):
        with self.assertRaises(Exception) as context:
            self.car.drive(200)
        self.assertEqual(str(context.exception), "You don't have enough fuel to drive!")
