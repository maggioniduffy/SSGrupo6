import pygame
import time
particle_radius = 3
position_delta = 80

factor = 500
width, height = 700, 700

def draw_silo(screen, L, W, D):
    left = width/2 - W/2
    top = height/2 - L/2
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(left, top, W, L),  1)
    pygame.draw.line(screen, (0,0,0), (left+((W-D)/2), top + L), (left+((W+D)/2), top+L), 4)


def animate():
    pygame.init()
    print('init')
    r = 255
    g = 255
    b = 255

    screen = pygame.display.set_mode((height, width))
    
    bg = 0, 0, 0

    screen.fill(bg)
    
    f = open('./output.txt', 'r')
    lines = f.read()
    f.close()
    first_line = lines.split("\n")[0].split(" ")
    L = float(first_line[0]) * factor
    W = float(first_line[1]) * factor
    D = float(first_line[2]) * factor
    iterations = lines.split("iteration\n")
    left = width/2 + W/2
    top = height/2 + L/2
    # last_iter = iterations[-1].split("\n")
    # del last_iter[-1]
    # iterations[-1] = "\n".join(last_iter)
    del iterations[0]
    for iter in iterations:
        screen.fill(bg)
        draw_silo(screen, L, W, D)
        iter = iter[:-1]
        # time.sleep(0.5)
        for line in iter.split("\n"):
            data = line.split(" ")
            # print(data)
            radius = float(data[0]) * factor
            posx = float(data[1]) * factor
            posy = float(data[2]) * factor
            pygame.draw.circle(screen, (255,255,255), (left - posx, top - posy), radius)
            pygame.display.flip()
    time.sleep(3)

animate()