import open3d as o3d
import open3d.visualization.gui as gui
import open3d.visualization.rendering as rendering
import platform
import threading
import time
import sys
from constants import nxC, nyC, nzC

from constants import centerX, centerY, centerZ

sys.setrecursionlimit(10**8)
isMacOS = (platform.system() == "Darwin")

class GameOfLife:
    MENU_RANDOM = 2
    MENU_QUIT = 3

    def __init__(self):
        self._id = 0
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
        bbox = o3d.geometry.AxisAlignedBoundingBox([0, 0, 0],
                                    [nxC, nyC, nzC])
        self.scene.setup_camera(60, bbox, [centerX, centerY, centerZ])
        self.window.add_child(self.scene)

        f = open('./output.txt')
        data = f.read()
        f.close()
        self.gens = data.split('new gen\n')
        self.iteration = 0

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
                # macOS will name the first menu item for the running application
                # (in our case, probably "Python"), regardless of what we call
                # it. This is the application menu, and it is where the
                # About..., Preferences..., and Quit menu items typically go.
                menu.add_menu("Example", app_menu)
                menu.add_menu("Debug", debug_menu)
            else:
                menu.add_menu("Run", debug_menu)
            gui.Application.instance.menubar = menu

        self.window.set_on_menu_item_activated(GameOfLife.MENU_RANDOM,
                                self._on_menu_random)
        self.window.set_on_menu_item_activated(GameOfLife.MENU_QUIT,
                                self._on_menu_quit)  
    def update_geometry(self):
        self.scene.scene.clear_geometry()
        self.animate()
        #widget.scene.add_geometry('frame', frame, mat)
        #widget.scene.add_geometry('mesh', mesh, mat)   

    def add_sphere(self,x,y,z):
        difX = abs(x-centerX)
        difY = abs(y-centerY)
        difZ = abs(z-centerZ)
        if difX > difY and difX > difZ:
            dif = difX
        elif difY > difX and difY > difZ:
            dif = difY
        else:
            dif = difZ

        dif = dif * 0.1 if dif >= 0 else 0.9
        self._id += 1
        mat = rendering.MaterialRecord()
        mat.base_color = [
            0.9,
            0.1,
            0.9-dif, 1.0
        ]
        mat.shader = "defaultLit"
        sphere = o3d.geometry.TriangleMesh.create_sphere(0.4)
        sphere.compute_vertex_normals()
        sphere.translate([
            x * 1.0, y * 1.0,
            z * 1.0
        ])
        self.scene.scene.add_geometry("sphere" + str(self._id), sphere, mat)

    def animate(self):
        print(self.iteration, len(self.gens))
        lines = self.gens[self.iteration].split('\n')
        for line in lines:
            cell = line.split(',')
            if cell[0] != '':
                x,y,z,state= float(cell[0]),float(cell[1]),float(cell[2]),float(cell[3])
                if state == 1:
                    self.add_sphere(x,y,z)
            
    def _on_menu_random(self):
        def thread_main():
            for g in range(0,len(self.gens)-1):
                #print(g)
                gui.Application.instance.post_to_main_thread(self.window, self.update_geometry)
                self.iteration += 1
                time.sleep(0.1)
            time.sleep(15)
            
        threading.Thread(target=thread_main).start()

    def _on_menu_quit(self):
        self.set()

def main():
    gui.Application.instance.initialize()
    GameOfLife()
    gui.Application.instance.run()


if __name__ == "__main__":
    main()