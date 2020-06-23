import unittest

def addTaxAndPrice(taxAmount, originalPrice):
    return taxAmount + originalPrice;


class TestNumMethod(unittest.TestCase):
    
    def test_getTotalPrice(self):
        self.assertEqual(10.7, addTaxAndPrice(0.7, 10));

if __name__ == "__main__":
    unittest.main()
