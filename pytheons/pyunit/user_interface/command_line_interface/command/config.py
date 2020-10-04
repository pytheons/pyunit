import os

import yaml

from pytheons.pyunit.user_interface.command_line_interface.command.abstract import Command


class ConfigCommand(Command):
    class IndentationDumper(yaml.Dumper):

        def increase_indent(self, flow=False, indentless=False):
            return super(self.__class__, self).increase_indent(flow, False)

    def init(self, *options):
        defined_options = {
            'path': '--path'
        }
        path = None
        if options.__contains__(defined_options.get('path')):
            for option in options:
                option: str
                if option == defined_options.get('path'):
                    path = True
                    continue
                if option.__contains__('-'):
                    break
                if path:
                    path = option

        if path is None:
            path = os.getcwd()

        full_file_name = f'{path}/tests.yaml'
        if not os.path.exists(full_file_name):
            with open(full_file_name, 'w') as file:
                yaml.dump(data={'suites': ['default']}, stream=file, Dumper=self.IndentationDumper)
