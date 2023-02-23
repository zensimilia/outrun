import math
import time
import pygame
import random
from pygame.locals import HWSURFACE, DOUBLEBUF, RESIZABLE

WIDTH = 360
HEIGHT = 200
HALF_W = WIDTH / 2
HALF_H = HEIGHT / 2

PIVOT_X = WIDTH / 2
PIVOT_Y = HEIGHT - 40

FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PI = math.pi
TWO_PI = math.pi * 2
RADIUS = 145
SEGMENTS = 16
SPEEDS = [0.1, 0.5, -1, -0.5, 1, 3]


def send_signal(surface: pygame.Surface, delay):
    t = time.time() % delay / 2
    r = 500 * (math.tan(PI / 2 * t))
    pygame.draw.circle(surface, WHITE, (PIVOT_X, PIVOT_Y), r, 3)
    pygame.draw.circle(surface, WHITE, (PIVOT_X, PIVOT_Y), r - 16, 1)
    pygame.draw.circle(surface, WHITE, (PIVOT_X, PIVOT_Y), r - 32, 1)


def draw_arcs(surface: pygame.Surface, time):
    for n in range(4):
        shift = n * 90
        pygame.draw.arc(
            surface,
            WHITE,
            (
                PIVOT_X - RADIUS / 2 - 5,
                PIVOT_Y - RADIUS / 2 - 5,
                RADIUS + 10,
                RADIUS + 10,
            ),
            TWO_PI / 360 * (75 + shift) - time,
            TWO_PI / 360 * (105 + shift) - time,
        )
        pygame.draw.arc(
            surface,
            WHITE,
            (
                PIVOT_X - RADIUS + 10,
                PIVOT_Y - RADIUS + 10,
                RADIUS * 2 - 20,
                RADIUS * 2 - 20,
            ),
            TWO_PI / 360 * (22.5 + shift) - time,
            TWO_PI / 360 * (67.5 + shift) - time,
        )


def update(current, target, dt, duration):
    delta = target - current
    delta = delta * (duration / dt)
    return current + delta


def main():
    """
    Main function. The code goes running there.
    """
    pygame.init()
    pygame.font.init()
    # my_font = pygame.font.SysFont('Comic Sans MS', 10)
    mainsurface = pygame.display.set_mode(
        (WIDTH, HEIGHT), HWSURFACE | DOUBLEBUF | RESIZABLE
    )
    screen = pygame.Surface((WIDTH, HEIGHT))
    pygame.display.set_caption("Aliens Motion Tracker")
    clock = pygame.time.Clock()
    t = 1.0
    dt = time.time()
    rand = 0
    speed = 1.0

    running = True

    while running:
        ms = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        # t = 2 * math.atan(math.tan((time.monotonic() - PI) / 2)) + PI  # loop
        # t = 0
        # t = time.time()

        if time.time() >= dt + 1:
            rand = random.choice(SPEEDS)
            dt = time.time()

        speed = update(speed, rand, ms, 0.5)
        t = speed

        pygame.draw.circle(screen, WHITE, (PIVOT_X, PIVOT_Y), RADIUS - 3, 1)
        pygame.draw.circle(screen, WHITE, (PIVOT_X, PIVOT_Y), RADIUS / 2, 1)

        # draw arcs
        draw_arcs(screen, t)

        # draw segments
        for i in range(SEGMENTS):
            # z = i * (360/SEGMENTS) * ( TWO_PI / 360 ) - (2*math.atan(math.tan(t/2)))
            z = i * (360 / SEGMENTS) * (TWO_PI / 360) - t
            px = int(RADIUS * math.sin(z) + PIVOT_X)
            py = int(RADIUS * math.cos(z) + PIVOT_Y)

            d = -75
            if i % (SEGMENTS / 8):
                d = -10
            if (i % (SEGMENTS / 4)) and not (i % (SEGMENTS / 8)):
                d = -(RADIUS / 3 * 2)
                pygame.draw.circle(
                    screen,
                    WHITE,
                    ((d - 4) * math.sin(z) + px, (d - 4) * math.cos(-z) + py),
                    4,
                    1,
                )

            pygame.draw.line(
                screen,
                WHITE,
                (px, py),
                (d * math.sin(z) + px, d * math.cos(-z) + py),
            )

        send_signal(screen, delay=2)

        # Scale and update display
        w, h = pygame.display.get_surface().get_size()
        mainsurface.blit(pygame.transform.scale(screen, (w, h)), (0, 0))
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
