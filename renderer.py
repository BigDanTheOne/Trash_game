from students import *
import consts
import pygame
from unit import *
from images import *
from map import *
class Renderer:
    def __init__(self, battlefield: pygame.Surface, action_scene: pygame.Surface, screen: pygame.Surface,
                 static_scene: pygame.Surface):
        self.static_scene = static_scene
        self.screen = screen
        self.battlefield = battlefield
        self.action_scene = action_scene

    def render_static_unit(self, u: Unit):
        x = u.bbox.x
        y = u.bbox.y
        u.rescale()
        image = u.imgBody
        self.action_scene.blit(image, (x   - u.imgBody.get_size()[0] // 2, y   - u.imgBody.get_size()[1]))

    def render_all_units(self, units):
        self.action_scene.fill((0, 0, 0, 0))
        for unit in units:
            self.render_static_unit(unit)
            unit.draw_menu(self.action_scene)

    def render_going_unit(self, u: Unit, target, units):
        time = pygame.time.Clock()
        while u.moving:
            delta_t = time.tick_busy_loop() / 1000
            u.step(delta_t)
            self.render_all_units(units)
            self.update_screen(self.action_scene)

    def rotate_img(self, image, angle):
        """rotate a Surface, maintaining position."""

        loc = image.get_rect().center  # rot_image is not defined
        rot_sprite = pygame.transform.rotate(image, angle)
        rot_sprite.get_rect().center = loc
        return rot_sprite

    def render_background(self):
        self.static_scene.blit(background, (0, 0))


    def render_map(self, map: Map):
        for y in range(len(map.map_matrix)):
            for x in range(len(map.map_matrix[y])):
                pygame.draw.polygon(self.static_scene, pygame.Color(100, 100, 100) ,map.map_matrix[y][x].give_coordinates(), 1)

    def render_highlighted_cells(self, map: Map, my_cell_x, my_cell_y, cells, dist, student):
        self.battlefield.fill((0, 0, 0, 0))
        map.can_go_render(self.battlefield, my_cell_x, my_cell_y, cells, dist, student)

        x, y = pygame.mouse.get_pos()
        cell_x, cell_y = map.get_cell_by_x_y(x, y)

        pygame.draw.polygon(self.battlefield, pygame.Color(255, 255, 255), map.map_matrix[cell_y][cell_x].give_coordinates(), 1)
        self.update_screen(self.battlefield)

    def update_screen(self, updated):
        self.screen.blit(self.static_scene, (0, 0))
        self.screen.blit(self.battlefield, (0, 0))
        self.screen.blit(self.action_scene, (0, 0))
        pygame.display.update()
        pygame.event.pump()  # возможно не нужно



