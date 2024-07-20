import unittest
from simple_calculator import SimpleCalculator

class  TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(10, 6), 16)
        
    def test_subtract(self):
        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.subtract(2, 3), -1)
        #self.assertEqual(self.calc.subtract(5, 7), 2)
        
    def test_multiply(self):
        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(5, 5), 25)
        
    def test_divide(self):
        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.divide(10, 1), 10)
        self.assertEqual(self.calc.divide(18, 2), 9)
        