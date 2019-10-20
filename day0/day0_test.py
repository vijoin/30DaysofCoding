import unittest

from day0 import hello_world

class HelloWorldTest(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world('Hello, World.'), 'Hello, World.')