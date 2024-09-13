from OpenGL.GL import *
import numpy as np

vertices = np.array([
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1],
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1]
], dtype=float)

colors = [
    [1, 0, 0],  # Red
    [0, 1, 0],  # Green
    [0, 0, 1],  # Blue
    [1, 1, 0],  # Yellow
    [1, 0, 1],  # Magenta
    [0, 1, 1]   # Cyan
]

faces = [
    [0, 1, 2, 3],  # Front face
    [3, 2, 6, 7],  # Top face
    [7, 6, 5, 4],  # Back face
    [4, 5, 1, 0],  # Bottom face
    [5, 6, 2, 1],  # Right face
    [7, 4, 0, 3]   # Left face
]

def draw_cube(vertices):
    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        glColor3fv(colors[i])
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()
