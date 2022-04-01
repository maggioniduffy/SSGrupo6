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

    def set(self):
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
        self.window = gui.Application.instance.create_window(
            "Game of life", 1024, 768)
        self.scene = gui.SceneWidget()
        self.scene.scene = rendering.Open3DScene(self.window.renderer)
        self.scene.scene.set_background([0, 0, 0, 1])
        self.scene.scene.scene.set_sun_light(
            [-1, -1, -1],
            [1, 1, 1],
            100000)
        self.scene.scene.scene.enable_sun_light(True)
        bbox = o3d.geometry.AxisAlignedBoundingBox([-10, -10, -10],
                                                   [10, 10, 10])
        self.scene.setup_camera(60, bbox, [0, 0, 0])

        self.window.add_child(self.scene)

        if gui.Application.instance.menubar is None:
            if isMacOS:
                app_menu = gui.Menu()
                app_menu.add_item("Quit", GameOfLife.MENU_QUIT)
            debug_menu = gui.Menu()
            debug_menu.add_item("Add Random Spheres", GameOfLife.MENU_RANDOM)
            if not isMacOS:
                debug_menu.add_separator()
                debug_menu.add_item("Quit", GameOfLife.MENU_QUIT)

            menu = gui.Menu()
            if isMacOS:
                menu.add_menu("Example", app_menu)
                menu.add_menu("Debug", debug_menu)
            else:
                menu.add_menu("Run", debug_menu)
            gui.Application.instance.menubar = menu

        self.window.set_on_menu_item_activated(GameOfLife.MENU_RANDOM,
                                               self._on_menu_random)
        self.window.set_on_menu_item_activated(GameOfLife.MENU_QUIT,
                                               self._on_menu_quit)
        self._id += 1
        mat = rendering.Material()
        mat.base_color = [
            0.9,
            0.9,
            0.9, 1.0
        ]
        mat.shader = "defaultLit"
        sphere = o3d.geometry.TriangleMesh.create_sphere(5)
        sphere.compute_vertex_normals()
        sphere.translate([
            self.centerX * 1.0, self.centerY* 1.0,
            0.0
        ])
        self.scene.scene.add_geometry("sphere" + str(self._id), sphere, mat)            
    def __init__(self):
        self.set()

    def add_sphere(self):
        x, y, t = self.x, self.y, round(time.time() - self.initial_t)
        difX = abs(x-self.centerX)
        difY = abs(y-self.centerY)
        dif = difX if difX > difY else difY
        dif = dif * 0.05 if dif >= 0 else 0.9
        self._id += 1
        mat = rendering.Material()
        mat.base_color = [
            0.9,
            0.1,
            0.9-dif, 1.0
        ]
        mat.shader = "defaultLit"
        sphere = o3d.geometry.TriangleMesh.create_sphere(0.5)
        sphere.compute_vertex_normals()
        sphere.translate([
            x * 1.0, y * 1.0,
            t * 10.0
        ])
        self.scene.scene.add_geometry("sphere" + str(self._id), sphere, mat)

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
    
    def _on_menu_random(self):
        def thread_main():
            time.sleep(1)
            if not self.stop:
                gui.Application.instance.post_to_main_thread(self.window, self.get_alives)

        threading.Thread(target=thread_main).start()

    def _on_menu_quit(self):
        self.set()

def main():
    gui.Application.instance.initialize()
    GameOfLife()
    gui.Application.instance.run()


if __name__ == "__main__":
    main()