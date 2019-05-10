from images import *
import pygame

black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]


def draw_menu(screen, unit, point, type):
    if type == 'student':
        if unit.sex == 'man':
            color = red
            fon = fon1['student']['man']
        else:
            color = blue
            fon = fon1['student']['woman']
        fon = pygame.transform.scale(fon, (menu_x, menu_y))
    else:
        color = green
        fon = fon1[type]
        fon = pygame.transform.scale(fon, (menu_x, menu_y))
        if unit.face != None:
            face = pygame.image.load(unit.face)
            face = pygame.transform.scale(face, (face_x, face_y))
            fon.blit(face, [menu_x / 2 + (menu_x / 2 - face_x) / 2, menu_y / 2 - face_x / 2])

    point1 = [0, (menu_y - shrift_size * len(unit.stats)) / 2]

    for x in unit.stats:
        f2 = pygame.font.SysFont('serif', shrift_size)
        fon.blit(f2.render(x + " : " + str(unit.stats[x]), 1, color), point1)
        point1[1] += shrift_size
    screen.blit(fon, point)