import numpy as np

def spherical_to_cartesian(phi, theta, r):
    """ Convert spherical coordinates into x,y,z
    """
    x = np.sin(phi)*np.cos(theta)*r
    y = np.sin(phi)*np.sin(theta)*r
    z = np.cos(phi)*r
    return x, y, z

def latlon_to_spherical(latitude, longitude):
    """ Convert lat, lon to spherical coords.
    """
    phi = ((latitude - 90)/180.0) * np.pi
    theta = (longitude/360.0) * np.pi * 2
    return phi, theta

def latlon_to_cartesian(latitude, longitude, radius):
    """ Convert lat, lon to spherical coordinates, and then convert to cartesian
        returns x, y, z
    """
    return spherical_to_cartesian(*latlon_to_spherical(latitude, longitude), radius)

