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


### Attention! - Not full implement yet

-  `--suites` argument for `pyunit run` and `test suites runner`
