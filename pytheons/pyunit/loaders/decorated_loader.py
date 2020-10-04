import unittest.case
from typing import Type, Sequence
from unittest import TestLoader

from pytheons.pyunit.decorators.register import marked_as_test


class DecoratedLoader(TestLoader):

    def getTestCaseNames(self, testCaseClass: Type[unittest.case.TestCase]) -> Sequence[str]:
        functions = [function for function in dir(testCaseClass) if callable(getattr(testCaseClass, function))]
        test_fn_names = list(filter(lambda fn: marked_as_test(testCaseClass, fn), functions))

        return test_fn_names
