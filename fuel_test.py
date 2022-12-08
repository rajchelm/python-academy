from basics.oop.calculate_fuel import calculate_fuel

class MyTestCase(unittest.TestCase):

    def test_12(self):
        self.assertEqual(calculate_fuel(12), 2)

    def test_14(self):
        self.assertEqual(calculate_fuel(4), 2)

    def test_1969(self):
            self.assertEqual(calculate_fuel(1969), 654)

    def test_100756(self):
            self.assertEqual(calculate_fuel(100756), 33583)

    def test_0(self):
            self.assertEqual(calculate_fuel(0), 0)

if __name__ == '__main__':
    unittest.main()
