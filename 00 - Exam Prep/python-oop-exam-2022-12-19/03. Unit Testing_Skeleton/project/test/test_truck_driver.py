from project.truck_driver import TruckDriver
import unittest


class TestTruckDriver(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver('John', 200)

    def test_init_correct(self):
        self.assertEqual(self.driver.name, 'John')
        self.assertEqual(self.driver.money_per_mile, 200)
        self.assertEqual(self.driver.available_cargos, {})
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)

    def test_earned_money(self):
        self.driver.earned_money = 300
        self.assertEqual(self.driver.earned_money, 300)

    def test_earned_money_fails_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.driver.earned_money = -3
        self.assertEqual(str(ex.exception),"John went bankrupt.")

    def test_add_cargo_offer_already_in_exception(self):
        self.driver.add_cargo_offer("sofia", 300)
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("sofia", 300)
        self.assertEqual(str(ex.exception), "Cargo offer is already added.")

    def test_add_cargo_offer_added_correctly(self):
        result = self.driver.add_cargo_offer("sofia", 300)
        self.assertEqual(self.driver.available_cargos, {"sofia": 300})
        self.assertEqual(result, "Cargo for 300 to sofia was added as an offer.")



if __name__ == '__main__':
    unittest.main()
