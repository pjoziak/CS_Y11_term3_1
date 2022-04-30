from typing import Tuple
import pygame


class Window:
    WIDTH = 1000
    HEIGHT = 1000
    SIZE = (WIDTH, HEIGHT)


class Colors:
    PINK = (255, 20, 147)
    GREEN = (0, 255, 0)


class Gravity:
    Earth = (9.81, 0)


class Object:
    def __init__(
        self,
        x: float,
        y: float,
        height: float,
        width: float,
        v_x: float,
        v_y: float,
        boundary_x: float,
        boundary_y: float,
        color: Tuple[int, int, int],
    ):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.width = width
        self.height = height
        self.boundary_x = boundary_x
        self.boundary_y = boundary_y
        self.color = color

    def update(self, acceleration: Tuple[float, float], timestep: float):
        a_x, a_y = acceleration
        self.v_x += a_x * timestep
        self.v_y += a_y * timestep
        self.x += self.v_x * timestep
        self.y += self.v_y * timestep
        if self.x + self.height / 2 >= self.boundary_x or self.x - self.height / 2 <= 0:
            self.v_x = -self.v_x
        if self.y + self.width / 2 >= self.boundary_y or self.y - self.width / 2 <= 0:
            self.v_y = -self.v_y

    def draw(self, surface):
        rect = pygame.Rect(
            self.y - self.width / 2, self.x - self.height / 2, self.width, self.height
        )
        pygame.draw.rect(surface, self.color, rect)


def main():
    obj = Object(
        x=100,
        y=100,
        height=40,
        width=40,
        v_x=0,
        v_y=0,
        boundary_x=Window.HEIGHT,
        boundary_y=Window.WIDTH,
        color=Colors.PINK,
    )
    obj2 = Object(
        x=200,
        y=300,
        height=40,
        width=40,
        v_x=25,
        v_y=-60,
        boundary_x=Window.HEIGHT,
        boundary_y=Window.HEIGHT,
        color=Colors.PINK,
    )
    timestep = 100
    pygame.init()
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode(
        Window.SIZE
    )  # Displaying on specified window size
    pygame.display.set_caption("Our game")
    run = True
    while run:
        clock.tick(timestep)
        surface.fill(Colors.GREEN)  # Window Bg

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # To quit on clicking the X
                run = False
        obj.update(Gravity.Earth, timestep / 1000)
        obj2.update(Gravity.Earth, timestep / 1000)
        obj.draw(surface)
        obj2.draw(surface)
        pygame.display.update()  # To update the display with newly added codes

    pygame.quit()


main()
