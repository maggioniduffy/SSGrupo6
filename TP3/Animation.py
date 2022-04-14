import pygame
SIDE_SIZE = 6;
SMALL_RADIUS = 0.2;
BIG_RADIUS = 0.7;
def animate():
    pygame.init()
    width, height = SIDE_SIZE * 100, SIDE_SIZE * 100
    screen = pygame.display.set_mode((height, width))

    bg = 25, 25, 25

    screen.fill(bg)

    f = open('./output.txt', 'r')
    matrix = f.read()
    f.close()
    collisions = matrix.split('Collision\n')
    side = SIDE_SIZE * 100
    y = 0
    for g in range(1, len(collisions)):
        lines = collisions[g].split('\n')
        time = lines[0];
        screen.fill(bg)
        for line in range(1,len(lines)-1):
            index = lines[line].split(':')
            coordinates = index[1].split(',')
            x,y = float(coordinates[0]) * 100, float(coordinates[1]) * 100
            if (index[0] == '0'): #GRANDE
                pygame.draw.circle(screen, (255,0,0), (x, y), BIG_RADIUS * 100)
            else: #CHICAS
                pygame.draw.circle(screen, (255,255,255), (x, y), SMALL_RADIUS * 100)
        pygame.display.flip()
    while True:
        pass

animate()
