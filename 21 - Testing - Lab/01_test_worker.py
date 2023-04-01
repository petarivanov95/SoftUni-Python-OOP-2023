import unittest


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class WorkerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = Worker('John', 1000, 100)

    def test_init(self):
        self.assertEqual(self.worker.name, 'John')
        self.assertEqual(self.worker.salary, 1000)
        self.assertEqual(self.worker.energy, 100)
        self.assertEqual(self.worker.money, 0)

    def test_energy_increment_with_rest(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 101)

    def test_work_with_negative_energy(self):
        with self.assertRaises(Exception) as e:
            worker = Worker('John', 1000, -1)
            worker.work()
        self.assertEqual(str(e.exception), 'Not enough energy.')

    def test_salary_increase_with_work_method(self):
        self.worker.work()
        self.assertEqual(self.worker.money, 1000)

    def test_energy_decrease_with_work_method(self):
        self.worker.work()
        self.assertEqual(self.worker.energy, 99)

    def test_get_info_method(self):
        result = self.worker.get_info()
        expected_result = 'John has saved 0 money.'
        self.assertEqual(result,expected_result)



if __name__ == '__main__':
    unittest.main()
