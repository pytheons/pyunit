import unittest
from unittest import TestCase

from pytheons.pyunit.decorators.test import test


class ExampleTest(TestCase):
    @test
    def something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
