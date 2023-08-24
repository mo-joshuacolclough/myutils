import matplotlib.pyplot as plt
from myutils.maths.coords import latlon_to_cartesian

def plot_field_level_3d(ax, longitude, latitude, level_vals, height, **kwargs):
    """ Plot a single level of a field
    """
    x, y, z = latlon_to_cartesian(latitude, longitude, height)
    plot_obj = ax.scatter(x, y, z, c=level_vals, **kwargs)
    return plot_obj

def plot_lonlats_3d(ax, lons, lats, height=1.01, **kwargs):
    return plot_field_level(ax, lons, lats, (1.0, 1.0, 1.0, 0.5), height, **kwargs)

# --- 2D ---

def plot_field_level_2d(longitude, latitude, level_vals, **kwargs):
    po = plt.scatter(latitude, longitude, c=level_vals, **kwargs)
    plt.xlim(-180.0, 180.0)
    plt.ylim(-90.0, 90.0)
    plt.gca().set_aspect('equal')
    return po
