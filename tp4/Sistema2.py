import pygame
import time
particle_size = 3
def draw_particles(screen):
    posx = 100
    posy = 100
    d = 1e-8
    factor = 3125000000
    particle_count = 0
    stop = False
    line_count = 0
    colors = [(0,0,255), (255,0,0)]
    while(not stop):
        if particle_count < 16:
            pygame.draw.circle(screen, colors[(particle_count + line_count)%2] , (posx, posy), particle_size)
            posx = posx + d*factor
            particle_count += 1
        else:
            line_count += 1
            particle_count = 0
            posy = posy + d*factor
            posx = 100

        if line_count == 16:
            stop = True
    return

def animate():
    pygame.init()
    print('init')
    r = 255
    g = 255
    b = 255

    d = 1e-8
    factor = 3125000000

    width, height = 650, 650
    screen = pygame.display.set_mode((height, width))

    bg = 25, 25, 25

    screen.fill(bg)
    
    f = open('./rmi.txt', 'r')
    lines = f.read()
    f.close()
    iterations = lines.split("dt\n")[1:]
    #print(iterations)
    dts = [dt[0] for dt in  [line.split(":\n") for line in iterations]]
    positions = [pos[1].split("\n")[0] for pos in  [line.split(":\n") for line in iterations]]
    #print(positions)
    for index, _ in enumerate(range(0, len(iterations))):
        #print('step: ', index)
        screen.fill(bg)
        draw_particles(screen)
        posx = float(positions[index].split(" ")[0]) * factor + 100
        #print(posx)
        posy = float(positions[index].split(" ")[1]) * factor + 100
        #print(posy)
        pygame.draw.circle(screen, (255,255,255), (posx, posy), particle_size)
        pygame.display.flip()
    while True:
        pass

animate()
