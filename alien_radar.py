import math
import time
import pygame
from pygame.locals import HWSURFACE, DOUBLEBUF, RESIZABLE

WIDTH = 360
HEIGHT = 200
HALF_W = WIDTH / 2
HALF_H = HEIGHT - 20

PIVOT_X = WIDTH / 2
PIVOT_Y = HEIGHT - 40

FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

TWO_PI = math.pi * 2
PI = math.pi
SWEEP_LENGTH = 145
DOTS = 16


def send_signal(surface: pygame.Surface, delay):
    t = time.time() % delay / 2
    r = 500 * (math.tan(PI / 2 * t))
    pygame.draw.circle(surface, WHITE, (PIVOT_X, PIVOT_Y), r, 3)
    pygame.draw.circle(surface, WHITE, (PIVOT_X, PIVOT_Y), r - 16, 1)
    pygame.draw.circle(surface, WHITE, (PIVOT_X, PIVOT_Y), r - 32, 1)


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
    t = 0

    running = True

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        t = 2 * math.atan(math.tan((time.monotonic() - PI) / 2)) + PI  # loop
        # t = 0

        screen.fill(BLACK)

        pygame.draw.circle(
            screen, WHITE, (PIVOT_X, PIVOT_Y), SWEEP_LENGTH - 3, 1
        )
        pygame.draw.circle(
            screen, WHITE, (PIVOT_X, PIVOT_Y), SWEEP_LENGTH / 2, 1
        )

        for n in range(4):
            shift = n * 90
            pygame.draw.arc(
                screen,
                WHITE,
                (
                    PIVOT_X - SWEEP_LENGTH / 2 - 5,
                    PIVOT_Y - SWEEP_LENGTH / 2 - 5,
                    SWEEP_LENGTH + 10,
                    SWEEP_LENGTH + 10,
                ),
                TWO_PI / 360 * (75 + shift) - t,
                TWO_PI / 360 * (105 + shift) - t,
            )
            pygame.draw.arc(
                screen,
                WHITE,
                (
                    PIVOT_X - SWEEP_LENGTH + 10,
                    PIVOT_Y - SWEEP_LENGTH + 10,
                    SWEEP_LENGTH * 2 - 20,
                    SWEEP_LENGTH * 2 - 20,
                ),
                TWO_PI / 360 * (22.5 + shift) - t,
                TWO_PI / 360 * (67.5 + shift) - t,
            )

        for i in range(DOTS):
            # z = i * (360/DOTS) * ( TWO_PI / 360 ) - (2*math.atan(math.tan(t/2)))
            z = i * (360 / DOTS) * (TWO_PI / 360) - t
            px = int((SWEEP_LENGTH) * math.sin(z) + PIVOT_X)
            py = int((SWEEP_LENGTH) * math.cos(z) + PIVOT_Y)

            d = -75
            if i % (DOTS / 8):
                d = -10
            if (i % (DOTS / 4)) and not (i % (DOTS / 8)):
                d = -(SWEEP_LENGTH / 3 * 2)
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
                ((d) * math.sin(z) + px, (d) * math.cos(-z) + py),
            )

        send_signal(screen, delay=2)

        # Scale and update display
        w, h = pygame.display.get_surface().get_size()
        mainsurface.blit(pygame.transform.scale(screen, (w, h)), (0, 0))
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
