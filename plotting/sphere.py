import numpy as np

from myutils.maths.coords import spherical_to_cartesian

def gen_sphere(n_segments_complex):
    phi, theta = np.mgrid[0.0:np.pi:n_segments_complex, 0.0:2.0*np.pi:n_segments_complex]
    return phi, theta

def draw_sphere(ax, radius=1.0, **kwargs):
    phi, theta = gen_sphere(15j)
    x, y, z = spherical_to_cartesian(phi, theta, radius)
    ax.plot_surface(x, y, z, rstride=1, cstride=1, linewidth=0, shade=False, **kwargs)

