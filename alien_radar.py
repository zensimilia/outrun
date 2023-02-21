import math
import time
import pygame
from pygame.locals import HWSURFACE, DOUBLEBUF, RESIZABLE

WIDTH = 360
HEIGHT = 200
HALF_W = WIDTH / 2
HALF_H = HEIGHT - 20

FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

TWO_PI = math.pi * 2
PI = math.pi
SWEEP_LENGTH = 128
DOTS = 12

def main():
    """
    Main function. The code goes running there.
    """
    pygame.init()
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 10)
    mainsurface = pygame.display.set_mode((WIDTH, HEIGHT), HWSURFACE | DOUBLEBUF | RESIZABLE)
    screen = pygame.Surface((WIDTH, HEIGHT))
    pygame.display.set_caption("Circle")
    clock = pygame.time.Clock()
    t=0

    running = True


    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        pygame.draw.circle(screen, WHITE, (HALF_W, HALF_H), SWEEP_LENGTH, 1)
        # pygame.draw.circle(screen, WHITE, (HALF_W, HALF_H), SWEEP_LENGTH/4, 1)
        # pygame.draw.circle(screen, WHITE, (HALF_W, HALF_H), SWEEP_LENGTH/4*2, 1)
        pygame.draw.circle(screen, WHITE, (HALF_W, HALF_H), SWEEP_LENGTH/2, 1)

        # t += (1 % FPS) / FPS # loop
        t = 2 * math.atan(math.tan(time.monotonic() / 2)) # loop

        pygame.draw.arc(screen, WHITE, ((WIDTH-200)/2, 10, 200,50), 0+t, PI+t)

        for i in range(DOTS):
            # z = i * (360/DOTS) * ( TWO_PI / 360 ) - (2*math.atan(math.tan(t/2)))
            z = i * (360/DOTS) * ( TWO_PI / 360 ) - t
            text_surface = my_font.render(f'{z}', False, WHITE)
            px = int((SWEEP_LENGTH) * math.sin(z) + HALF_W)
            py = int((SWEEP_LENGTH) * math.cos(z) + HALF_H)
            # screen.blit(text_surface, (px,py))
            if (i % (DOTS/4)):
                d = -40
            else:
                # pygame.draw.line(screen, WHITE, (HALF_W,HALF_H), (px, py))
                d = -(SWEEP_LENGTH/3*2)

            pygame.draw.line(screen, WHITE, (px,py), ((d)*math.sin(z) + px, (d)*math.cos(-z)+py))
            # screen.set_at((px,py), WHITE)

        x = SWEEP_LENGTH * math.sin(-t) + HALF_W
        y = SWEEP_LENGTH * math.cos(t) + HALF_H

        # pygame.draw.line(screen,WHITE,(HALF_W, HALF_H), (x,y), 3)

        # Scale and update display
        w, h = pygame.display.get_surface().get_size()
        mainsurface.blit(pygame.transform.scale(screen, (w, h)), (0, 0))
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
