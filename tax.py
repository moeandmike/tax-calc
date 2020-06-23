import unittest

def addNums(num1, num2):
    return num1 + num2;

def getTax(num1):
    return round(.07 * num1, 2);

class TestNumMethod(unittest.TestCase):
    
    def test_addNums(self):
        self.assertEqual(7, addNums(3, 4));

    def test_getTax(self):
        self.assertEqual(.70, getTax(10));

if __name__ == "__main__":
    unittest.main()
