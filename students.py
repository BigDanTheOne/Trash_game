from consts import *
from renderer import *
from unit import *
import images
import random
import pygame
import math
import copy


class Bilet:
    global subjects

    def __init__(self, add_quastion):
        if add_quastion == True:
            self.topic = None
            self.task1 = random.choice(subjects)
        else:
            self.topic = random.choice(subjects)
            self.task1 = random.choice(subjects)
            self.task2 = random.choice(subjects)


class Menu:
    def __init__(self, given_player, dificulty):
        self.dificulty = dificulty
        self.player = given_player
        self.end = False
        # TODO: calling the griphical interface of Menu

    def getParametr(self):
        'info we got froom the griphical interface'
        while True:
            print('choose one of these:'
                  'luck from 0 to {} '
                  'frequency  from 0 to {} '
                  'time_bot from 0 to {} '
                  'alcohol from 0 to {} '
                  'if the choice is done print exit 0'.format(int(10 / self.dificulty), int(10 / self.dificulty),
                                                              int(10 / self.dificulty), int(10 / self.dificulty)))
            type, value = input().split()
            if type == 'exit':
                self.end = True
                break
            if type not in ('luck', 'frequency', 'time_bot', 'alcohol') and int(value) not in range(
                    int(10 / self.dificulty)):
                print('incorrect input')
            else:
                break
        return type, int(value)


class BBox:
    def __init__(self, x: float, y: float, radius: float):
        self.x = x
        self.y = y
        self.r = radius

    def intersect(self, x: int, y: int):
        return (x - self.x) ** 2 + (y - self.y) ** 2 <= self.r ** 2


class Student(Unit):
    def __init__(self, index):
        self.type = 'student'
        self.stats = dict()
        super().__init__(index)
        # print('I am a Student')

    def answer(self, bilet):
        pass

    def askAnswer(self, student, bilet):
        pass

    def giveAnswer(self, student, bilet):
        pass

    def giveStats(self):
        'There we have some formula, which computes stats, now its only simple sum'
        ans = 0
        # print(self.stats)
        for i in self.stats:
            if i != 'faculty':
                ans += int(self.stats[i])
        return ans

    def select_unit(self, unit: Unit):
        pass


class Player(Student):
    def __init__(self, *args):
        # TODO: add default stats
        super().__init__()
        # print('I am a Student')


class Bot(Student):
    def __init__(self, difficulty, index):
        # print('I am a Bot')
        super().__init__(index)
        self.subject = random.choice(subjects)
        self.luck = int(random.normalvariate(student_stat / difficulty, 2) % 10)
        self.intelect = int(random.normalvariate(student_stat / difficulty, 2) % 10)
        self.oratory = int(random.normalvariate(student_stat / difficulty, 2) % 10)
        self.sex = random.choice(('man', 'woman'))
        self.friendliness = int(random.normalvariate(student_stat / difficulty, 2) % 10)
        self.stats['subject'] = self.subject
        self.stats['luck'] = self.luck
        self.stats['intelect'] = self.intelect
        self.stats['oratory'] = self.oratory
        self.stats['sex'] = self.sex
        self.stats['friendliness'] = self.friendliness
        # TODO: add skills


class BotFactory:
    'there you can choose a Favourity subject and a difficulty of the game from 1 to 5'
    'the higher the complexity the lower the characteristics of the allies'

    def __init__(self, subject, difficulty, index):
        self.index = index
        self.subject = subject
        self.difficulty = difficulty

    def createUnit(self):
        self.index+=1
        return Bot(self.difficulty, self.index)


class PlayerFactory:
    class builder:
        def __init__(self, player, menu):
            self.player = player
            self.menu = menu

        def fillField(self):
            type, value = self.menu.getParametr()
            if type != 'exit':
                # self.Player.type = value
                self.player.stats[type] = value
            print('now your total power is: ', self.player.giveStats())

    def __init__(self, subject, difficulty):
        self.my_player = Player()
        self.my_menu = Menu(self.my_player, difficulty)
        self.my_builder = PlayerFactory.builder(self.my_player, self.my_menu)
        self.my_player.subject = subject
        self.my_player.stats['subject'] = subject
        while self.my_menu.end != True:
            self.my_builder.fillField()

    def createUnit(self):
        return self.my_player


def giveStudentFacroty(manager, subject, difficulty):
    'args for manager: "Player", "Bot"'
    # print('creating an abstract Student')
    if manager == 'Player':
        return PlayerFactory(subject, difficulty)
    elif manager == 'Bot':
        return BotFactory(subject, difficulty, index)
    else:
        raise TypeError

# my_factory1 = giveStudentFacroty('Bot', 'DIHT', 2)
# my_factory2 = giveStudentFacroty('Player', 'DIHT', 2)
# my_bot = my_factory1.createUnit()
# my_player = my_factory2.createUnit()
# print(my_bot.__dict__)
# print(my_player.__dict__)
