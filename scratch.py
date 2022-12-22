import unittest
import requests

class PokemonTest(unittest.TestCase):

    def setUp(self) -> None:
        self.url = "https://pokeapi.co/api/v2/pokemon"

    def test_list_of_pokemon(self):
        params = {
            "limit": 100000,
            "offset": 0
        }
        res_body = requests.get(self.url).json()

        self.assertEqual(25, len(res_body))
        self.assertEqual(1, res_body[0]["id"])
        self.assertEqual(25, res_body[-1]["id"])



if __name__ == '__main__':
    unittest.main()