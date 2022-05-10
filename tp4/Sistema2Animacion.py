import pygame
import time
particle_radius = 3
position_delta = 80
def draw_particles(screen):
    d = 1e-8
    factor = 3125000000
    particle_count = 0
    stop = False
    line_count = 0
    colors = [(0,0,255), (255,0,0)]
    posx = position_delta + d*factor
    posy = position_delta
    while(not stop):
        if particle_count < 16:
            pygame.draw.circle(screen, colors[(particle_count + line_count)%2] , (posx, posy), particle_radius)
            posx = posx + d*factor
            particle_count += 1
        else:
            line_count += 1
            particle_count = 0
            posy = posy + d*factor
            posx = position_delta + d*factor

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

    width, height = 700, 700
    screen = pygame.display.set_mode((height, width))

    bg = 0, 0, 0

    screen.fill(bg)
    
    f = open('./rmi.txt', 'r')
    lines = f.read()
    f.close()
    iterations = lines.split("t\n")[1:]
    #print(iterations)
    dts = [dt[0] for dt in  [line.split(":\n") for line in iterations]]
    positions = [pos[1].split("\n")[0] for pos in  [line.split(":\n") for line in iterations]]
    #print(positions)
    for index, _ in enumerate(range(0, len(iterations))):
        #print('step: ', index)
        time.sleep(0.003)
        screen.fill(bg)
        draw_particles(screen)
        posx = float(positions[index].split(" ")[0]) * factor + position_delta
        #print(posx)
        posy = float(positions[index].split(" ")[1]) * factor + position_delta
        #print(posy)
        pygame.draw.circle(screen, (255,255,255), (posx, posy), particle_radius)
        pygame.display.flip()
    time.sleep(3)

animate()
