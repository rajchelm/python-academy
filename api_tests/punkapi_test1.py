import unittest
import requests


class PunkAPITest(unittest.TestCase):
    def test_get_default_beers(self):
        res_body = requests.get("https://api.punkapi.com/v2/beers?page=2&per_page=80").json()

        self.assertEqual(80, len(res_body))
        self.assertEqual(81, res_body[0]["id"])
        self.assertEqual(160, res_body[-1]["id"])

    # def test_beer_123(self):
    #     res_body = requests.get("https://api.punkapi.com/v2/beers/123").json()
    #     self.assertEqual(123, res_body[0]["0"])
    #     self.assertEqual(1, len(res_body))



if __name__ == '__main__':
    unittest.main()
