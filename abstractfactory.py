from examenator import *
from students import *

class AbstractFactory:
    index = 0
    def give_concret_factory(self, name, *args):
        if name == 'lecturer':
            return lecturers_factory(*args, self.index)
        elif name == 'seminarist':
            return seminarists_factory(*args, self.index)
        elif name == 'Player':
            return PlayerFactory(*args, self.index)
        elif name == 'Bot':
            return BotFactory(*args, self.index)



