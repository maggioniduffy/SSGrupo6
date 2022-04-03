def workspace_divider(needed: int):
    from math import sqrt
    while int(sqrt(needed)) != sqrt(needed):
        needed += 1
    return int(sqrt(needed))

def create_matplotlib_graphs(space_object: Space, generations: int, save: tuple = (False, None), show: bool = True,
                             onebyone: bool = False):
    """
    This function will create matplotlib figures for both saving and displaying at every generation.
    :param space_object: The Space object
    :param generations: An integer of generation number
    :param save: A tuple which is (will_save, file_name_prefix). Default is (False, None)
    :param show: True if want to show, False if don't want.
    :param onebyone: True if show one by one and False for showing together.
    :return:
    """
    # Making imports here because of unnecessary usage
    # of matplotlib
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    # Creating the first values without .update()
    values = Space.clear_ndarray(space_object.export())

    if not onebyone:
        fig = plt.figure()
        workspace_dims = workspace_divider(generations)
        for gen in range(generations):
            fig.add_subplot(110 * workspace_dims + gen + 1, projection="3d")
            ax = fig.gca()
            ax.set_aspect('auto')
            ax.voxels(values, edgecolor="k")
            if save[0]:
                plt.savefig(f"{save[1]}_gen_{gen}")

            space_object.update()
            values = Space.clear_ndarray(space_object.export())

        if show:
            plt.show()
    else:
        for gen in range(generations):
            fig = plt.figure(gen)
            ax = fig.gca(projection='3d')
            ax.set_aspect('auto')
            ax.voxels(values, edgecolor="k")
            if save[0]:
                plt.savefig(f"{save[1]}_gen_{gen}")
            if show:
                print("You must close the figure in order to see next generation.")
                plt.show()

            space_object.update()
            values = Space.clear_ndarray(space_object.export())
