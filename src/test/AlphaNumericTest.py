from ..main import AlphaNumericMethod
import unittest

class AlphaNumericTest(unittest.Testcase):
    def test_alpha_numeric(self):
        self.assertEqual(self.generate(), 'hi');

if __name__ == "main":
    unittest.main();