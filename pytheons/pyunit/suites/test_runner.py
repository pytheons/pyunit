from pytheons.pyunit.user_interface.command_line_interface.command.run import RunCommand


class TestRunner:
    @staticmethod
    def run():
        RunCommand().handle()
