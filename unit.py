from strategy import *
from menu_stats import *
from consts import *
from images import *
import pygame
import images
import copy
import math
import random


class BBox:
    def __init__(self, x: float, y: float, radius: float):
        self.x = x
        self.y = y
        self.r = radius

    def intersect(self, x: int, y: int):
        return (x - self.x) ** 2 + (y - self.y) ** 2 <= self.r ** 2


class Unit:
    # imgHeadad':  pygame.Surface
    # imgBody:  pygame.Surface
    # bbox: BBox(100, 100, 10)
    # speed: int = unitSpeed

    # def __init__(self, imgHead, imgBody):
    #     self.imgHead = pygame.image.load(imgHead)
    #     self.imgBody = pygame.image.load(imgBody)
    def __init__(self, index):
        self.index = index
        self.health = random.choice(health[self.type])
        self.stats['health'] = self.health
        self.bbox = BBox(100, 100, bbox_r)
        self.speed: int = unitSpeed
        self.imgHead:  pygame.Surface = head[self.type]
        self.imgBody:  pygame.Surface = body[self.type]
        self.imgBody0: pygame.Surface = body[self.type]
        self.w_0: int = self.imgBody.get_size()[0]
        self.h_0: int = self.imgBody.get_size()[1]
        self.target: BBox = BBox(-1, -1, 0)
        self.moving: bool = False

    def __eq__(self, other):
        return abs(self.bbox.x - other.bbox.x) + abs(self.bbox.y - other.bbox.y) == 0

    def rescale(self):
        self.imgBody = pygame.transform.scale(self.imgBody0,
                                              (int(self.w_0 * (H - battlefield_zero_point[1] + self.bbox.y) // H),
                                               int(self.h_0 * (H - battlefield_zero_point[1] + self.bbox.y) // H)))

    def distance_to_target(self):
        return math.sqrt((self.target.x - self.bbox.x) ** 2 + (self.target.y - self.bbox.y) ** 2)

    def step(self, delta_t):
        if self.moving:
            new_bbox = copy.deepcopy(self.bbox)
            print(self.bbox.x, self.bbox.y)
            new_bbox.x += self.speed * math.sin(
                math.atan2(self.target.x - self.bbox.x, self.target.y - self.bbox.y)) * delta_t
            new_bbox.y += self.speed * math.cos(
                math.atan2(self.target.x - self.bbox.x, self.target.y - self.bbox.y)) * delta_t
            # Checking that the target is achieved
            if self.distance_to_target() < self.speed * delta_t:
                self.moving = False
                new_bbox = copy.deepcopy(self.target)
                self.target.x = self.target.y = -1

            self.bbox = BBox(new_bbox.x, new_bbox.y, bbox_r)

            # Jumping animation
            # self.spriteoffset = 2 * ((self.time * 20) % 5)
        # self.time += delta_t

    def go_to(self, target):
        self.target = BBox(target[0], target[1], 0)
        self.moving = True
        self.time = 0

    def intersect(self, x: int, y: int):
        return self.bbox.intersect(x, y)

    hit = hit1

    def move(self, target, delta_t):
        pass


    def draw_menu(self, screen):
        x, y = pygame.mouse.get_pos()
        if self.bbox.intersect(x, y) and pygame.mouse.get_pressed()[2]:
            draw_menu(screen, self, [screen_widt - menu_x, 0], self.type)
            pygame.display.update()