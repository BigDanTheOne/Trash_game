from enum import Enum
import pygame

pygame.init()
pygame.font.init()

screen_height = pygame.display.Info().current_h
screen_widt = pygame.display.Info().current_w
battlefield_width = screen_widt // 1.9
battlefield_height = screen_height // 3.5
battlefield_zero_point = (350, screen_height - 100)
N_x, N_y = 5, 5
cell_height = battlefield_height / N_y
H = 600


class person:
    def __init__(self, p_name, p_subject, p_sex='man', p_picture=None):
        self.name = p_name
        self.subject = p_subject
        self.picture = p_picture
        self.sex = p_sex

    def __eq__(self, other):
        if type(other) == person and self.subject == other.subject and self.name == other.name:
            return True
        else:
            return False


class Subjects(Enum):
    OKTCH = 'OKTCH'
    matan = 'matan'
    matlog = 'matlog'


class Manager(Enum):
    bot = 'bot'
    player = 'player'


unitSpeed = 150
student_stat = 10
max_stat = 10
dist = 6
bbox_r = 20
health = dict()
health['student'] = range(100, 200)
health['seminarist'] = range(200, 300)
health['lecturer'] = range(300, 400)
lecturer_knowlege = 10
lecturer_easiness = 10
seminarist_knowlege = 7
seminarist_easiness = 7
lecturer_friendliness = 7
seminarist_friendliness = 7
lecturer_alcohol_liking = 7
seminarist_alcohol_liking = 7
subjects = ['matan', 'OKTCH', 'matlog']
seminarists = dict()
seminarists['matan'] = [
    person('Ivanova', 'matan', 'woman', p_picture='Images/ivanova.jpg'),
    person('Kuzmenko', 'matan', p_picture='Images/kuzmenko.png'),
    person('Starodubcev', 'matan')]
seminarists['OKTCH'] = [person('Grigoriev', 'OKTCH', p_picture='Images/grigoriev.png'), person('Glibenchuk', 'OKTCH'),
                        person('Iliinskiy', 'OKTCH', p_picture='Images/ilinskiy.png')]
seminarists['matlog'] = [person('Irhin', 'matlog'), person('Milovanov', 'matlog'), person('Ivachenko', 'matlog')]

lecturers_name = [person('Musatov', 'mathlog', p_picture='Images/musatov.png'),
                  person('Raygor', 'OKTCH', p_picture='Images/raygor.png'),
                  person('Redkozubov', 'matan', p_picture='Images/redkozubov.png')]
