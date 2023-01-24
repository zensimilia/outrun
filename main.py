"""
Synthwave/retrowave/vaporwave digital art

MIT License
Copyright (c) 2023 Di M Dub
"""
import pygame
from pygame.locals import HWSURFACE, DOUBLEBUF, RESIZABLE

WIDTH = 128
HEIGHT = 96
HALF_W = WIDTH / 2
HALF_H = HEIGHT / 2

FPS = 15
SPEED = 50

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def easeInExpo(t) -> float:
    """
    The function takes a param and returns a value that is a exponent of param.

    :param t: The current time (or position) of the tween. This can be seconds
    or frames, steps, whatever – as long as the unit is the same
    as is used for the total time
    :return: the value of the function at the given point
    """
    return (pow(2, 8 * t) - 1) / 255

def main():
    """
    Main function. The code goes running there.
    """
    pygame.init()
    mainsurface = pygame.display.set_mode((WIDTH, HEIGHT), HWSURFACE | DOUBLEBUF | RESIZABLE)
    screen = pygame.Surface((WIDTH, HEIGHT))
    pygame.display.set_caption("Synthwave graphics")
    clock = pygame.time.Clock()

    running = True
    rx, rdx = 0, 1
    linesZ = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        # The Sun
        pygame.draw.circle(screen, WHITE, [HALF_W, 38], 20)
        pygame.draw.line(screen, BLACK, [34, 34], [160, 34], 1)
        pygame.draw.line(screen, BLACK, [34, 38], [160, 38], 2)
        pygame.draw.line(screen, BLACK, [34, 42], [160, 42], 3)
        pygame.draw.line(screen, BLACK, [34, 47], [160, 47], 4)

        # Mountains left
        pygame.draw.line(screen, WHITE, [0, 43], [10, 36], 1)
        pygame.draw.line(screen, WHITE, [10, 36], [14, 42], 1)
        pygame.draw.line(screen, WHITE, [11, 47], [21, 30], 1)
        pygame.draw.line(screen, WHITE, [21, 30], [27, 40], 1)
        pygame.draw.line(screen, WHITE, [21, 43], [32, 37], 1)
        pygame.draw.line(screen, WHITE, [32, 37], [46, 47], 1)

        # Mountains right
        pygame.draw.line(screen, WHITE, [81, 47], [97, 40], 1)
        pygame.draw.line(screen, WHITE, [97, 40], [99, 45], 1)
        pygame.draw.line(screen, WHITE, [97, 42], [103, 33], 1)
        pygame.draw.line(screen, WHITE, [103, 33], [109, 47], 1)
        pygame.draw.line(screen, WHITE, [106, 42], [115, 33], 1)
        pygame.draw.line(screen, WHITE, [115, 33], [120, 38], 1)
        pygame.draw.line(screen, WHITE, [116, 43], [128, 25], 1)

        # Horizont
        pygame.draw.rect(screen, BLACK, pygame.Rect(0, HALF_H, WIDTH, HEIGHT))
        pygame.draw.line(screen, WHITE, [0, HALF_H], [WIDTH, HALF_H], 1)

        # Vertical lines (left to right)
        rx += rdx
        if rx > 20:
            rdx = -1
        if rx < -20:
            rdx = 1
        pygame.draw.line(screen,  WHITE, [20, HALF_H], [0, 52  + rx/6], 1)
        pygame.draw.line(screen,  WHITE, [38, HALF_H], [0, 64 + rx/3], 1)
        pygame.draw.line(screen,  WHITE, [50, HALF_H], [6 + rx, HEIGHT], 2)
        pygame.draw.line(screen,  WHITE, [HALF_W, HALF_H], [HALF_W + rx, HEIGHT], 2)
        pygame.draw.line(screen,  WHITE, [78, HALF_H], [122 + rx, HEIGHT], 2)
        pygame.draw.line(screen,  WHITE, [90, HALF_H], [WIDTH, 64 - rx/3], 1)
        pygame.draw.line(screen,  WHITE, [108, HALF_H], [WIDTH, 52 - rx/6], 1)

        # Horizontal lines
        for i, _ in enumerate(linesZ):
            y = easeInExpo(linesZ[i] / 100) * SPEED + (HALF_H)
            if y > HALF_H + 2:
                pygame.draw.line(screen, WHITE, [0, y], [WIDTH, y], 1)
            linesZ[i] += 1
            if linesZ[i] >= 100:
                linesZ[i] = 0

        # Scale and update display
        w, h = pygame.display.get_surface().get_size()
        mainsurface.blit(pygame.transform.scale(screen, (w, h)), (0, 0))
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
