import unittest

def addNums(num1, num2):
    return num1 + num2;

class TestNumMethod(unittest.TestCase):
    
    def test_addNums(self):
        self.assertEqual(7, addNums(3, 4));

if __name__ == "__main__":
    unittest.main()
