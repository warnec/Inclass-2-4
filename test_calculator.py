import unittest
import calculator



#unsure why this code does not recognize the methods in calculator.  It imports it without eror yet fails on the last
#method call.  I have never imported a file with python im my life and this is my first python based class.  Im going
#to move onto the second module in the name of time.

class TestCase(unittest.TestCase):

    def test1(self):
        self.assertEqual(add(2, 1), 3)
    def test2(self):
        self.assertEqual(add(-4, -1), -5)
    def test3(self):
        self.assertEqual(subtract(2, 1), 1)
    def test4(self):
        self.assertEqual(subtract(-4, 1), -5)
    def test6(self):
        self.assertEqual(multiply(4, 5), 20)
    def test7(self):
        self.assertEqual(multiply(-4, 2), -8)
    def test8(self):
        self.assertEqual(divide(4, 1), 4)
    def test9(self):
        self.assertEqual(divide(6, 0), None)

    if __name__ == '__main__':
        unittest.main(verbosity=2)



