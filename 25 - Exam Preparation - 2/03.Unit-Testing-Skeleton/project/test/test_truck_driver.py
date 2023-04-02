from project.truck_driver import TruckDriver

import unittest


class TestTruckDriver(unittest.TestCase):
    def setUp(self) -> None:
        self.truck_driver = TruckDriver('John', 10)

    def test_init(self):
        self.assertEqual(self.truck_driver.name, 'John')
        self.assertEqual(self.truck_driver.money_per_mile, 10)
        self.assertEqual(self.truck_driver.available_cargos, {})
        self.assertEqual(self.truck_driver.earned_money, 0)
        self.assertEqual(self.truck_driver.miles, 0)

    def test_earned_money(self):
        self.truck_driver.earned_money = 3
        self.assertEqual(self.truck_driver.earned_money, 3)

    def test_earned_money_raise_error(self):
        with self.assertRaises(ValueError) as ex:
            self.truck_driver.earned_money = -1
        self.assertEqual(str(ex.exception), "John went bankrupt.")

    def test_add_cargo_offer(self):
        self.truck_driver.add_cargo_offer("Sofia", 100)
        self.assertEqual(self.truck_driver.available_cargos,{"Sofia":100})

    def test_add_cargo_offer_already_exists(self):
        self.truck_driver.add_cargo_offer("Sofia", 100)
        with self.assertRaises(Exception) as ex:
            self.truck_driver.add_cargo_offer("Sofia", 100)
        self.assertEqual(str(ex.exception),"Cargo offer is already added.")

    def test_drive_best_cargo_offer_error(self):
        self.assertEqual(self.truck_driver.drive_best_cargo_offer(), "There are no offers available.")

    def test_drive_best_cargo_offer(self):
        self.truck_driver.add_cargo_offer('Sofia', 100)
        self.truck_driver.add_cargo_offer('Varna', 200)
        # TODO Finish the Checker

        result = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(self.truck_driver.earned_money, 2000)
        self.assertEqual(self.truck_driver.miles, 200)
        self.assertEqual(result, 'John is driving 200 to Varna.')

    def test_eat(self):
        self.truck_driver.earned_money = 50
        self.truck_driver.eat(250)
        self.assertEqual(self.truck_driver.earned_money, 30)

    def test_sleep(self):
        self.truck_driver.earned_money = 100
        self.truck_driver.sleep(1000)
        self.assertEqual(self.truck_driver.earned_money, 55)

    def test_pump_gas(self):
        self.truck_driver.earned_money = 600
        self.truck_driver.pump_gas(1500)
        self.assertEqual(self.truck_driver.earned_money, 100)

    def test_repair_truck(self):
        self.truck_driver.earned_money = 10000
        self.truck_driver.repair_truck(10000)
        self.assertEqual(self.truck_driver.earned_money, 2500)

    def test_check_for_activities(self):
        self.truck_driver.earned_money = 11760
        result = self.truck_driver.check_for_activities(10000)

        self.assertEqual(self.truck_driver.earned_money, 10)

if __name__ == '__main__':
    unittest.main()
