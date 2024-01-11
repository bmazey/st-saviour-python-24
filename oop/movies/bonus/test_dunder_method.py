import unittest

class TestMyClassStrMethod(unittest.TestCase):
    def test_str_method(self):
        self.assertEqual(str(object), "MyClass instance with value: 42")

if __name__ == '_main_':
    unittest.main()