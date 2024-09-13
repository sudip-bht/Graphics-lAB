import numpy as np

def add_homogeneous_coordinate(vertices):
    return np.hstack((vertices, np.ones((vertices.shape[0], 1))))

def remove_homogeneous_coordinate(vertices):
    return vertices[:, :3]

def translate(vertices, x, y, z):
    T = np.array([
        [1, 0, 0, x],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1]
    ])
    return np.dot(vertices, T.T)

def rotate_x(vertices, angle):
    angle = np.radians(angle)
    cos_a = np.cos(angle)
    sin_a = np.sin(angle)
    R_x = np.array([
        [1, 0, 0, 0],
        [0, cos_a, -sin_a, 0],
        [0, sin_a, cos_a, 0],
        [0, 0, 0, 1]
    ])
    return np.dot(vertices, R_x.T)

def rotate_y(vertices, angle):
    angle = np.radians(angle)
    cos_a = np.cos(angle)
    sin_a = np.sin(angle)
    R_y = np.array([
        [cos_a, 0, sin_a, 0],
        [0, 1, 0, 0],
        [-sin_a, 0, cos_a, 0],
        [0, 0, 0, 1]
    ])
    return np.dot(vertices, R_y.T)

def rotate_z(vertices, angle):
    angle = np.radians(angle)
    cos_a = np.cos(angle)
    sin_a = np.sin(angle)
    R_z = np.array([
        [cos_a, -sin_a, 0, 0],
        [sin_a, cos_a, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    return np.dot(vertices, R_z.T)

def scale(vertices, sx, sy, sz):
    S = np.diag([sx, sy, sz, 1])
    return np.dot(vertices, S)

def shear(vertices, sh_xy, sh_xz, sh_yz):
    S = np.array([
        [1, sh_xy, sh_xz, 0],
        [0, 1, sh_yz, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    return np.dot(vertices, S.T)



def apply_transformations(vertices, state):
    homogeneous_vertices = add_homogeneous_coordinate(vertices)
    transformed_vertices = translate(homogeneous_vertices, *state['translate'])
    transformed_vertices = rotate_x(transformed_vertices, state['rotate_x'])
    transformed_vertices = rotate_y(transformed_vertices, state['rotate_y'])
    transformed_vertices = rotate_z(transformed_vertices, state['rotate_z'])
    transformed_vertices = scale(transformed_vertices, *state['scale'])
    #transformed_vertices = shear(transformed_vertices, *state['shear'])
    return remove_homogeneous_coordinate(transformed_vertices)

