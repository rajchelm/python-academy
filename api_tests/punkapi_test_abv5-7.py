import unittest
import requests


class PunkAPITest(unittest.TestCase):
    def test_get_default_beers(self):
        res_body = requests.get("https://api.punkapi.com/v2/beers?abv_gt=4.9&abv_lt=7.1").json()

        # self.assertEqual(5, len(res_body))

        self.assertEqual(1, res_body[0]["id"])

        self.assertEqual(5, res_body[-1]["id"])




if __name__ == '__main__':
    unittest.main()
