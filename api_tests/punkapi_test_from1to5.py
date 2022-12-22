import unittest
import requests


class PunkAPITest(unittest.TestCase):
    def test_get_default_beers(self):
        res_body = requests.get("https://api.punkapi.com/v2/beers?ids=1|2|3|4|5").json()

        self.assertEqual(5, len(res_body))
        self.assertEqual(1, res_body[0]["id"])
        self.assertEqual(2, res_body[1]["id"])
        self.assertEqual(3, res_body[2]["id"])
        self.assertEqual(4, res_body[3]["id"])
        self.assertEqual(5, res_body[-1]["id"])




if __name__ == '__main__':
    unittest.main()
