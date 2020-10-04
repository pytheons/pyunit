import os
import unittest
from typing import Optional, List

from pytheons.pyunit.loaders.decorated_loader import DecoratedLoader
from pytheons.pyunit.user_interface.command_line_interface.command.abstract import Command


class RunCommand(Command):
    def handle(self, *args, **kwargs):
        defined_options = {
            'suites': '--suites'
        }

        suites = None
        if args.__contains__(defined_options.get('suites')):
            option: str
            for option in args:
                if option == defined_options.get('suites'):
                    suites = []
                    continue

                if option.__contains__('-'):
                    break

                if suites is not None:
                    suites.append(option)

        self.run(suites)

    @staticmethod
    def run(suites: Optional[List[str]] = None):
        loader = DecoratedLoader()
        runner = unittest.TextTestRunner()

        tests_path = '{workdir}/tests'.format(workdir=os.getcwd().replace('tests', ''))
        if suites is None:
            try:
                paths = list(map(lambda node: '{}/{}'.format(tests_path, node), os.listdir(tests_path)))
                suites = list(map(
                    lambda suit: suit.replace(os.path.dirname(suit), '').replace('/', ''),
                    list(filter(os.path.isdir, paths))
                ))
            except FileNotFoundError as error:
                print(error.strerror, '"{}"'.format(error.filename))
                return

        for suite_directory in suites:
            path = '{}/{}'.format(tests_path, suite_directory)
            if os.path.exists(path):
                directories = list(
                    filter(lambda directory_candidate: directory_candidate not in ['__pycache__'], os.listdir(path))
                )
                for directory in directories:
                    test_directory = '{}/{}'.format(path, directory)
                    try:
                        suite = loader.discover(start_dir=test_directory, pattern='*_test.py', top_level_dir='')
                        runner.run(suite)
                    except ImportError:
                        continue
