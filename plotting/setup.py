import matplotlib.pyplot as plt

def setup_axis_3d(limits):
    ax = plt.subplot(111, projection="3d")
    ax.set_xlim([-limits,limits])
    ax.set_ylim([-limits,limits])
    ax.set_zlim([-limits,limits])
    ax.set_box_aspect([1, 1, 1])
    return ax
