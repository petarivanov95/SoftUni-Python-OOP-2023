from project.vehicle import Vehicle
import unittest


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Vehicle(100, 120)

    def test_init(self):
        self.assertEqual(self.car.fuel, 100)
        self.assertEqual(self.car.capacity, 100)
        self.assertEqual(self.car.horse_power, 120)
        self.assertEqual(self.car.fuel_consumption, 1.25)

    def test_drive(self):
        self.car.drive(30)
        self.assertEqual(self.car.fuel, 62.5)

    def test_drive_insufficient(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual(str(ex.exception), "Not enough fuel")

    def test_refuel(self):
        self.car.fuel = 0
        self.car.refuel(40)
        self.assertEqual(self.car.fuel, 40)

    def test_refuel_exception(self):
        self.car.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.car.refuel(140)
        self.assertEqual(str(ex.exception), "Too much fuel")

    def test_str_representation(self):
        result = self.car.__str__()
        expected = f"The vehicle has 120 " \
                   f"horse power with 100 fuel left and 1.25 fuel consumption"
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
