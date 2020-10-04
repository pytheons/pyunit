# PyUnit library
This is wrapper for standard unittest library for Python with custom TestRunner to run test suites.
The main argument that this library was published is that standard unittest TestCase need test method prefix.
This way with TestCase method prefix introduce the noise and if you have a lot small test methods in TestCase
class then you still read test, and you are not focused on what do the test should test.
I prefer the `@test` decorator or other solutions out of test method name to tell Your tests which method 
is registered as test in test runner, then You can focused to read method as poetry not as technical layer.

This library contains tool called `pyunit` to:
- initiate the configuration file for suites
- run tests automatically by `pyunit run` from command line 

## Installation:
```shell script
user@host $ pip install pytheons.pyunit
```

## Usage
```shell script
user@host $ pyunit
--------------------------------------------------
PyUnit - unittest test runner based on annotation.

Usage: pyunit COMMAND --OPTION <argument>
  pyunit config init [--path=<path>]
  pyunit run [--suites=<suites>]
  pyunit (-h | --help)
  pyunit --version

Commands:
  config - Configuration sub-system
  suites - Tests Suites sub-system
  run    - Test runner from CLI

Options:
  -h --help     Show this screen.
  --version     Show version.

```

1. Create the configuration by command `pyunit config init [--path=path_to_your_test_configuration_dir]`
2. Create `.py` file to run all your tests. Below is content for this file:
    ```python
    from pytheons.pyunit.suites.test_runner import TestRunner
    
    TestRunner.run()
    ```
3. Write or Reorganise Your tests in structure `test/<suite-name>/[optional subdir]/<test_name>.py`
4. Each test folder should be a package with `__init__.py` file - unittest throws exception that directory
is not `executable` or `callable`
5. Mark Your method by `@test` decorator from PyUnit library
    ```python
    from unittest import TestCase
    from pytheons.pyunit.decorators.test import test
    
    class MyFirstTest(TestCase):
        @test
        def when_fuel_size_is_30_then_cost_should_be_300(self):
            fuel = 30
            self.assertEqual(300, FuelCalcuator.calculate(fuel))
    ```
6. Run test by `pyunit run` or run  `.py` file to run all tests

### Attention! - Not full implement yet

-  `--suites` argument for `pyunit run` and `test suites runner`
