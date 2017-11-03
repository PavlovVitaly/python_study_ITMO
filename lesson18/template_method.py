# Template method


from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    @abstractmethod
    def _do_execute(self):
        pass

    def execute(self):
        print('Before command.')
        self._do_execute()
        print('After command.')


class ListCommand(Command):
    def _do_execute(self):
        print('List of task.')


cmd = ListCommand()
cmd.execute()
