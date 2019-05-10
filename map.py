from enum import Enum
import consts
import pygame
import random
from pygame import *
from consts import *
from geometry import *
from menu_stats import *
import Comand
from students import *
import pygame.locals

pygame.init()
pygame.font.init()


class Cell:
    def __init__(self, cell_width_lower: int, cell_width_upper: int, cell_x: int, cell_y: int,
                 target_lower: (int, int), target_upper: (int, int)):
        """ polygon in tuple are ordered like this:
                 0 |  1
                -------
                 3 |  2
        """
        self.polygon: Polygon
        self.highlighted: bool = False
        self.cell_width_lower = cell_width_lower
        self.cell_width_upper = cell_width_upper
        self.cell_x = cell_x
        self.cell_y = cell_y
        self.polygon = Polygon(Point(target_lower[0], screen_height - target_lower[1]),
                               Point(target_lower[0] + cell_width_lower, screen_height - target_lower[1]),
                               Point(target_upper[0] + cell_width_upper, screen_height - target_upper[1]),
                               Point(target_upper[0], screen_height - target_upper[1]))
        # self.polygon[3] = (target_upper[0], screen_height - target_upper[1])
        # self.polygon[2] = (target_upper[0] + cell_width_upper, screen_height - target_upper[1])
        # self.polygon[1] = (target_lower[0] + cell_width_lower, screen_height - target_lower[1])
        # self.polygon[0] = (target_lower[0], screen_height - target_lower[1])

    def intersect(self, x: int, y: int):
        return self.polygon.encloses_point(Point(x, y))

    def give_coordinates(self):
        return [[self.polygon.vertices[0][0], self.polygon.vertices[0][1]],
                [self.polygon.vertices[1][0], self.polygon.vertices[1][1]],
                [self.polygon.vertices[2][0], self.polygon.vertices[2][1]],
                [self.polygon.vertices[3][0], self.polygon.vertices[3][1]]]

    def give_center(self):
        return int(self.polygon.centroid[0]), int(self.polygon.centroid[1])


class Map:
    map_matrix: list(list()) = []

    def __init__(self):
        self.hightlighted_cell_x = -1
        self.hightlighted_cell_y = -1
        for i in range(N_y):
            zero_target_i = (battlefield_zero_point[0] + (i * battlefield_width * cell_height) / (2 * H),
                             screen_height - battlefield_zero_point[1] + i * cell_height)
            zero_target_i_plus_1 = (battlefield_zero_point[0] + ((i + 1) * battlefield_width * cell_height) / (2 * H),
                                    screen_height - battlefield_zero_point[1] + (i + 1) * cell_height)
            cell_width_lower = battlefield_width * (H - i * cell_height) / (H * N_x)
            cell_width_upper = battlefield_width * (H - (i + 1) * cell_height) / (H * N_x)
            tmp = []
            for j in range(N_x):
                g = Cell(cell_width_lower, cell_width_upper, j, i,
                         (zero_target_i[0] + j * cell_width_lower, zero_target_i[1]),
                         (zero_target_i_plus_1[0] + j * cell_width_upper, zero_target_i_plus_1[1]))
                tmp.append(g)
            self.map_matrix.append(tmp)

    def get_cell_by_x_y(self, x, y):
        for i in range(len(self.map_matrix)):
            for j in range(len(self.map_matrix[i])):
                if self.map_matrix[i][j].intersect(x, y):
                    return j, i
        return -1, -1

    def get_x_y_by_cell(self, cell_x, cell_y):
        return self.map_matrix[cell_y][cell_x].give_center()

    def recognize_action(self, units, events):
        for event in events:
            if event.type == pygame.locals.QUIT or \
                    (event.type == pygame.locals.KEYDOWN and
                     event.key == pygame.locals.K_ESCAPE):
                return Comand.Exit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    x, y = pygame.mouse.get_pos()
                    for unit in units:
                        if unit.intersect(x, y):
                            return Comand.SelectUnit(unit)
                        cell_x, cell_y = self.get_cell_by_x_y(x, y)
                        if cell_x != -1 and cell_y != -1:
                            return Comand.GoTo(self.map_matrix[cell_y][cell_x].give_center()[0],
                                               self.map_matrix[cell_y][cell_x].give_center()[1], unit)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return True

    def can_go_render(self, screen, my_cell_x, my_cell_y, cells, unit_dist, unit):
        unit_x , unit_y = self.get_cell_by_x_y(unit.bbox.x, unit.bbox.y)
        for x in self.map_matrix:
            for cell in x:
                if abs(cell.cell_x - my_cell_x) + abs(cell.cell_y - my_cell_y) < unit_dist and not cells[cell.cell_x][
                    cell.cell_y]:
                    vertexes = cell.give_coordinates()
                    pygame.draw.polygon(screen, blue, cell.give_coordinates())
                    for i in range(4):
                        pygame.draw.line(screen, green, vertexes[i], vertexes[(i + 1) % 4])
                elif abs(cell.cell_x - unit_x) + abs(cell.cell_y - unit_y) == 0:
                    vertexes = cell.give_coordinates()
                    pygame.draw.polygon(screen, red, cell.give_coordinates())
                    for i in range(4):
                        pygame.draw.line(screen, blue, vertexes[i], vertexes[(i + 1) % 4])
        pygame.display.update()
