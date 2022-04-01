import open3d as o3d
import open3d.visualization.gui as gui
import open3d.visualization.rendering as rendering
import platform
import threading
import time

isMacOS = (platform.system() == "Darwin")

class GameOfLife:
    MENU_RANDOM = 2
    MENU_QUIT = 3
    def __init__(self) -> None:
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
        self.scene.setup_camera(60, bbox, [self.centerX, self.centerY, 0])

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
        
    def add_sphere(self,x,y,z):
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
            y * 1.0
        ])
        self.scene.scene.add_geometry("sphere" + str(self._id), sphere, mat)

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