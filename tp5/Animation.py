# import pygame
# import time
# particle_radius = 3
# position_delta = 80

# factor = 500
# width, height = 1000, 1000

# def draw_silo(screen, L, W, D):
#     left = width/2 - W/2
#     top = height/2 - L/2
#     pygame.draw.rect(screen, (255,255,255), pygame.Rect(left, top, W + 1, L + 1),  1)
#     pygame.draw.line(screen, (0,0,0), (left+((W-D)/2), top + L), (left+((W+D)/2), top+L), 4)


# def animate():
#     pygame.init()
#     print('init')
#     r = 255
#     g = 255
#     b = 255

#     screen = pygame.display.set_mode((height, width))
    
#     bg = 0, 0, 0

#     screen.fill(bg)
    
#     f = open('./output022.txt', 'r')
#     lines = f.read()
#     f.close()
#     first_line = lines.split("\n")[0].split(" ")
#     L = float(first_line[0]) * factor + 1
#     W = float(first_line[1]) * factor + 1
#     D = float(first_line[2]) * factor + 1
#     iterations = lines.split("iteration\n")
#     print(len(iterations))
#     left = width/2 + W/2
#     top = height/2 + L/2
#     # last_iter = iterations[-1].split("\n")
#     # del last_iter[-1]
#     # iterations[-1] = "\n".join(last_iter)
#     del iterations[0]
#     for iter in iterations:
        

#         iter = iter[:-1]
#         time.sleep(0.001)
#         draw_silo(screen, L, W, D)
#         for line in iter.split("\n"):
#             data = line.split(" ")
#             # print(data)
#             radius = float(data[0]) * factor
#             posx = float(data[1]) * factor
#             posy = float(data[2]) * factor
#             pygame.draw.circle(screen, (0,100,255), (left - posx, top - posy), radius)

#         pygame.display.flip()
#         screen.fill(bg)
#         # time.sleep(0.05)
#     time.sleep(3)

# animate()
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation
import numpy as np

# Read the text file
with open('output010.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

    # Parse the silo dimensions
    silo_height, silo_width, hole_diameter = map(float, lines[0].split())
    lines.remove(lines[0])
    # Initialize the figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Set limits for the plot
    ax.set_xlim(0, silo_width)
    ax.set_ylim(0, silo_width)
    ax.set_zlim(0, silo_height)

    # Define the silo walls
    silo_vertices = np.array([
        [0, 0, 0],
        [0, silo_width, 0],
        [silo_width, silo_width, 0],
        [silo_width, 0, 0],
        [0, 0, silo_height],
        [0, silo_width, silo_height],
        [silo_width, silo_width, silo_height],
        [silo_width, 0, silo_height]
    ])

    silo_faces = np.array([
        [0, 1, 2, 3],
        [0, 4, 7, 3],
        [0, 1, 5, 4],
        [1, 2, 6, 5],
        [2, 3, 7, 6],
        [4, 5, 6, 7]
    ])

    # Create a collection of polygons for the silo walls
    silo_polygons = [silo_vertices[silo_faces[0]],
                    silo_vertices[silo_faces[1]],
                    silo_vertices[silo_faces[2]],
                    silo_vertices[silo_faces[3]],
                    silo_vertices[silo_faces[4]],
                    silo_vertices[silo_faces[5]]]

    silo_collection = Poly3DCollection(silo_polygons, facecolor='gray', alpha=0.5)
    ax.add_collection3d(silo_collection)

    # Create a circle for the hole
    hole_center = [silo_width / 2, silo_width / 2]
    hole_radius = hole_diameter / 2
    theta = np.linspace(0, 2 * np.pi, 100)
    x = hole_center[0] + hole_radius * np.cos(theta)
    y = hole_center[1] + hole_radius * np.sin(theta)
    z = np.zeros_like(x)
    hole_line, = ax.plot(x, y, z, color='gray', linewidth=2)

    # Initialize the particles scatter plot
    particles_scatter = ax.scatter([], [], [], c='b', s=150, marker='o')

    iterations = []
    for line in lines:
        # print(line)
        if line == "iteration":
            iterations.append([])
            continue
        
        iterations[-1].append(line.split(' '))
    # def update(frame):
    #     global particles_scatter
    #     i = frame + 1

    #     for line in lines:
    #         data = line.split(" ")
    #         # print(data)
    #         if data[0] == "iteration":
    #             particles_scatter.set_offsets(np.empty((0, 3)))
    #             particles_scatter.set_sizes([])
    #             continue
    #         radius = float(data[0])
    #         posx = float(data[1])
    #         posy = float(data[2])
    #         posz = float(data[3])
            
    #         particle_pos = np.array([[posx, posy, posz]])
    #         particles_scatter.set_offsets(particle_pos)
    #         particles_scatter.set_sizes([radius])
    #         # print("line")
    #     return particles_scatter,
    iteration = 0
    def update(frame):
        global particles_scatter
        global iteration
        global ax
        new_x = []
        new_y = []
        new_z = []
        particles_scatter.set_offsets(np.empty((0, 3)))
        particles_scatter.set_sizes([])
        for line in iterations[iteration]:
            # print(data)
            radius = float(line[0])
            posx = float(line[1])
            posy = float(line[2])
            posz = float(line[3])
            
            new_x.append(posx)
            new_y.append(posy)
            new_z.append(posz)

            # print("line")
        particles_scatter = ax.scatter(new_x, new_z, new_y , c='b', s=50, marker='o')

        iteration += 1
        return particles_scatter

    # Create the animation
    animation = FuncAnimation(fig, update, frames=len(iterations)-1 ,interval=1, blit=True)

    # Show the plot
    plt.show()

