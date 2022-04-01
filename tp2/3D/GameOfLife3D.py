import open3d as o3d
import open3d.visualization.gui as gui
import open3d.visualization.rendering as rendering
import platform
import threading
from random import randint, random, uniform
import numpy as np
import time
import sys
from math import floor

isMacOS = (platform.system() == "Darwin")

class GameOfLife:
    MENU_RANDOM = 2
    MENU_QUIT = 3
    if len(sys.argv) > 1:
        percentage = int(sys.argv[1])
    else:
        percentage = 0
    sys.setrecursionlimit(99999999)
    nxC, nyC = 50, 50
    centerX = nxC/2
    centerY = nyC/2
    center = np.array((centerX,centerY))
    factorx = nxC/5 * 4 - nxC/5
    factory = nyC/5 * 4 - nyC/5

    p_cells = floor(percentage * factorx * factory / 100)

    maxNeighs = 3
    minNeighs = 2

    def __init__(self):
        self.x = 0
        self.y = 0
        self.initial_t = time.time()
        self._id = 0
        self.stop = False
        self.gameState = np.zeros((GameOfLife.nxC, GameOfLife.nyC))
        for _ in range(0, GameOfLife.p_cells):
            x = randint(floor(GameOfLife.nxC/5), floor(GameOfLife.nxC/5)*4)
            y = randint(floor(GameOfLife.nyC/5), floor(GameOfLife.nyC/5)*4)
            while self.gameState[x, y] == 1:
                x = randint(floor(GameOfLife.nxC/5), floor(GameOfLife.nxC/5)*4)
                y = randint(floor(GameOfLife.nyC/5), floor(GameOfLife.nyC/5)*4)
            self.gameState[x, y] = 1
        self.newGameState = np.copy(self.gameState)
        self.t = 0
        self.distances = []
        self.maxDistance = 0
        self.alive_cells = GameOfLife.p_cells
        self.alive_cells_ev = [self.alive_cells]

    def get_alives(self):
        while not self.stop:
            time.sleep(1)
            for y in range(0, GameOfLife.nxC):
                for x in range(0, GameOfLife.nyC):
                    if not self.stop:
                        n_neigh = self.gameState[(x-1), (y-1)] if (x-1) > 0 and (y-1) > 0 else 0
                        n_neigh += self.gameState[(x), (y-1)] if (y-1) > 0 else 0
                        n_neigh += self.gameState[(x+1), (y-1)] if (x+1) < GameOfLife.nxC and (y-1) > 0 else 0
                        n_neigh += self.gameState[(x-1), (y)] if (x-1) > 0 else 0
                        n_neigh += self.gameState[(x+1), (y)] if (x+1) < GameOfLife.nxC else 0
                        n_neigh += self.gameState[(x-1), (y+1)] if (x-1) > 0 and (y+1) < GameOfLife.nyC else 0
                        n_neigh += self.gameState[(x), (y+1)] if (y+1) < GameOfLife.nyC else 0
                        n_neigh += self.gameState[(x+1), (y+1)] if (x+1) < GameOfLife.nxC and (y+1) < GameOfLife.nyC else 0

                        #Regla 1
                        if self.gameState[x, y] == 0 and n_neigh == GameOfLife.maxNeighs:
                            print('vive')
                            self.newGameState[x, y] = 1
                            self.alive_cells += 1
                        
                        #Regla 2
                        elif self.gameState[x, y] == 1 and (n_neigh <= GameOfLife.minNeighs or n_neigh > GameOfLife.maxNeighs):
                            print('muere')
                            self.newGameState[x, y] = 0
                            self.alive_cells -= 1
                    
                    if self.newGameState[x, y] == 1:
                        print('add')
                        point = np.array((x,y))
                        dist = np.linalg.norm(GameOfLife.center-point)
                        if dist > self.maxDistance:
                            self.maxDistance = dist
                        self.x = x
                        self.y = y
                        self.add_sphere()
                    if self.alive_cells == 0 or ((x == 0 or x == (GameOfLife.nxC - 1)) or (y == 0 or y == (GameOfLife.nyC - 1))) and self.newGameState[x, y] == 1:
                        self.stop = True
    