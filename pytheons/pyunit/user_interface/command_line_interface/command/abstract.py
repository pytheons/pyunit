from abc import ABCMeta


class Command(metaclass=ABCMeta):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__()
        self.handle(*args, **kwargs)

    def handle(self, *args, **kwargs):
        if len(args) > 0:
            subcommand: str = args[0]
            if hasattr(self, subcommand):
                getattr(self, subcommand)(*args[1:])


