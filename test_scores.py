import random
import unittest
import scores


class TestScores(unittest.TestCase):
    game_stamps = scores.generate_game()
    correct_stamp = {
        "offset": 11,
        "score": {
            "home": 5,
            "away": 7
        }
    }
    incorrect_stamp = {
        "offset": 0,
        "scores": {
            "home": 0,
            "away": 0
        }
    }
    number = random.randrange(len(game_stamps))
    result = (
        game_stamps[number]['score']['home'],
        game_stamps[number]['score']['away']
    )
    err_offset = game_stamps[-1]['offset'] + 1

    def test_offsets_get_score(self):
        for offset in ('', -2, 3.6, [], (3,), True):
            with self.assertRaises(ValueError) as error:
                scores.get_score(self.game_stamps, offset)
            self.assertEqual('Incorrect offset', str(error.exception))
        with self.assertRaises(ValueError) as error:
                scores.get_score(self.game_stamps, self.err_offset)
        self.assertEqual('There is no such offset', str(error.exception))

    def test_stamps_get_score(self):
        for stamp in ('', -2, 3.6, [], (3,), True, self.incorrect_stamp):
            with self.assertRaises(ValueError) as error:
                scores.get_score(stamp, 0)
            self.assertEqual('Incorrect game_stamps', str(error.exception))

    def test_return_get_score(self):
        self.assertEqual((5,7), scores.get_score([self.correct_stamp], 11))
        self.assertNotEqual((1,2), scores.get_score([self.correct_stamp], 11))
    
    def test_random_offset_get_score(self): 
        self.assertEqual(self.result, scores.get_score(self.game_stamps, self.number))


if __name__ == '__main__':
    unittest.main()
