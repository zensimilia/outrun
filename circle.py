import math
import pygame
from pygame.locals import HWSURFACE, DOUBLEBUF, RESIZABLE

WIDTH = 360
HEIGHT = 200
HALF_W = WIDTH / 2
HALF_H = HEIGHT / 2

FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

TWO_PI = math.pi * 2
PI = math.pi

def num_to_range(num, inMin, inMax, outMin, outMax):
  return outMin + (float(num - inMin) / float(inMax - inMin) * (outMax - outMin))

def draw_something(screen:pygame.Surface, q, t, color = WHITE, dx = HALF_W, dy = HALF_H):
    for i in range(360) :
        x = dx + 20*math.sin(q + t / FPS)
        y = dy + 20*math.cos(q + t / FPS)
        th = i * TWO_PI / 360;
        os = num_to_range(math.cos(th - TWO_PI * (t / 100)), -1, 1, 0, 1);
        os = 0.1 * pow(os, 2.75);
        r = 70 * (1 + os * math.cos(16 * th + 1.5 * TWO_PI * t / FPS + q));
        screen.set_at((int(r * math.sin(th) + x) , int(-r * math.cos(th) + y)), color)

def main():
    """
    Main function. The code goes running there.
    """
    pygame.init()
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


        t += 1
        draw_something(screen, 0, t+50, dx=WIDTH/3)
        draw_something(screen, math.pi, t, dx=WIDTH/3*2)

        # Scale and update display
        w, h = pygame.display.get_surface().get_size()
        mainsurface.blit(pygame.transform.scale(screen, (w, h)), (0, 0))
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
