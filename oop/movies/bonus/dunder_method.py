import unittest

class MyClass:
    def _init_(self,value):
        self.value = value

    def _str_(self):
        return f"MyClass instance with value: {self.value}"
    