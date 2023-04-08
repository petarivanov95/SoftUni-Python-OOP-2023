import unittest
from project.tennis_player import TennisPlayer


class TestTennisPlayer(unittest.TestCase):

    def setUp(self):
        self.player = TennisPlayer("Petar", 25, 1234.5)

    def test_init(self):
        self.assertEqual(self.player.name, "Petar")
        self.assertEqual(self.player.age, 25)
        self.assertEqual(self.player.points, 1234.5)
        self.assertEqual(self.player.wins, [])


    def test_name_error_validation(self):
        with self.assertRaises(ValueError) as ex:
            TennisPlayer("PT", 25, 1234.5)
        self.assertEqual(str(ex.exception),"Name should be more than 2 symbols!")

    def test_age_error_validation(self):
        with self.assertRaises(ValueError) as ex:
            TennisPlayer("Petar", 17, 1234.5)
        self.assertEqual(str(ex.exception),"Players must be at least 18 years of age!")


    def test_add_new_win(self):
        self.player.add_new_win('Wimbledon')
        self.assertEqual(self.player.wins, ['Wimbledon'])

    def test_add_new_win_already_added(self):
        self.player.add_new_win('Wimbledon')
        result = self.player.add_new_win('Wimbledon')
        self.assertEqual(result, "Wimbledon has been already added to the list of wins!")


    def test_lt_operator_higher_points(self):
        player2 = TennisPlayer("Nadal", 22, 2000.0)
        result = self.player < player2
        expected_str = "Nadal is a top seeded player and he/she is better than Petar"
        self.assertEqual(result, expected_str)

    def test_lt_operator_lower_points(self):
        player2 = TennisPlayer("Djokovic", 22, 1000.0)
        result = self.player < player2
        expected_str = "Petar is a better player than Djokovic"
        self.assertEqual(result, expected_str)

    def test_lt_operator_same_points(self):
        player2 = TennisPlayer("Nadal", 22, 1234.5)
        result = self.player < player2
        expected_str = "Petar is a better player than Nadal"
        self.assertEqual(result, expected_str)

    def test_str_representation_with_no_wins(self):
        player = TennisPlayer("Petar", 25, 1234.5)
        expected_str = "Tennis Player: Petar\nAge: 25\nPoints: 1234.5\nTournaments won: "
        self.assertEqual(str(player), expected_str)

    def test_str_representation_with_wins(self):
        player = TennisPlayer("Petar", 25, 1234.5)
        player.add_new_win("Wimbledon")
        player.add_new_win("US Open")
        expected_str = "Tennis Player: Petar\nAge: 25\nPoints: 1234.5\nTournaments won: Wimbledon, US Open"
        self.assertEqual(str(player), expected_str)

if __name__ == "__main__":
    unittest.main()
