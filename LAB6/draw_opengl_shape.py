import glfw
from OpenGL.GL import *
from cube_3dobject import draw_cube, vertices
from transformation import apply_transformations
from OpenGL.GLUT import *
from OpenGL.GLU import *
import threading
import time

projection_mode = 'perspective'

def custom_perspective():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (800 / 600), 1, 50.0)
    glMatrixMode(GL_MODELVIEW)

def custom_orthographic():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2, 2, -2, 2, 1, 10)
    glMatrixMode(GL_MODELVIEW)

def set_projection(mode):
    global projection_mode
    projection_mode = mode
    if projection_mode == 'perspective':
        custom_perspective()
    elif projection_mode == 'orthographic':
        custom_orthographic()

transformation_state = {
    'translate': [0.0, 0.0, 0.0],
    'rotate_x': 0.0,
    'rotate_y': 0.0,
    'rotate_z': 0.0,
    'scale': [1.0, 1.0, 1.0],
}

def key_callback(window, key, scancode, action, mods):
    if action == glfw.PRESS:
        if key == glfw.KEY_ESCAPE:
            glfw.set_window_should_close(window, True)

def apply_terminal_commands(command):
    global transformation_state, projection_mode
    commands = {
        'ESC': lambda: glfw.set_window_should_close(window, True),
        'UP': lambda: update_transform('translate', 1, 0.1),
        'DOWN': lambda: update_transform('translate', 1, -0.1),
        'LEFT': lambda: update_transform('translate', 0, -0.1),
        'RIGHT': lambda: update_transform('translate', 0, 0.1),
        'R': lambda: update_transform('rotate_y', None, 10.0),
        'Q': lambda: update_transform('rotate_x', None, 10.0),
        'W': lambda: update_transform('rotate_x', None, -10.0),
        'E': lambda: update_transform('rotate_z', None, 10.0),
        'T': lambda: update_transform('rotate_z', None, -10.0),
        'A': lambda: update_transform('scale', 0, 0.1),
        'S': lambda: update_transform('scale', 0, -0.1),
        'N': lambda: update_transform('scale', 1, 0.1),
        'M': lambda: update_transform('scale', 1, -0.1),
        'C': lambda: update_transform('scale', 2, 0.1),
        'V': lambda: update_transform('scale', 2, -0.1),
        'P': lambda: set_projection('perspective'),
        'O': lambda: set_projection('orthographic')
    }

    command_function = commands.get(command)
    if command_function:
        command_function()
    else:
        print(f"Unknown command: {command}")

def update_transform(transform_type, index, value):
    if index is not None:
        transformation_state[transform_type][index] += value
    else:
        transformation_state[transform_type] += value

def input_thread():
    while not glfw.window_should_close(window):
        print_menu()
        command = input("Enter command: ").strip().upper()
        apply_terminal_commands(command)

def print_menu():
    print("\nCommands:")
    print("UP, DOWN, LEFT, RIGHT: Translate")
    print("R: Rotate Y")
    print("Q: Rotate X+")
    print("W: Rotate X-")
    print("E: Rotate Z+")
    print("T: Rotate Z-")
    print("A: Scale X+")
    print("S: Scale X-")
    print("N: Scale Y+")
    print("M: Scale Y-")
    print("C: Scale Z+")
    print("V: Scale Z-")
    print("P: Perspective Projection")
    print("O: Orthographic Projection")
    print("ESC: Exit")

def display():
    global vertices
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    # Apply transformations
    transformed_vertices = apply_transformations(vertices, transformation_state)
    
    glTranslatef(0.0, 0.0, -10.0)
    glRotatef(transformation_state['rotate_x'], 1.0, 0.0, 0.0)
    glRotatef(transformation_state['rotate_y'], 0.0, 1.0, 0.0)
    glRotatef(transformation_state['rotate_z'], 0.0, 0.0, 1.0)
    glScalef(*transformation_state['scale'])
    
    draw_cube(transformed_vertices)

    glfw.swap_buffers(window)

def main():
    global window
    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "3D Transformations", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glEnable(GL_DEPTH_TEST)
    set_projection('orthographic')
    glfw.set_key_callback(window, key_callback)

    # Start the input thread
    threading.Thread(target=input_thread, daemon=True).start()

    while not glfw.window_should_close(window):
        display()
        glfw.poll_events()
        time.sleep(0.01)  # To reduce CPU usage

    glfw.terminate()

if __name__ == "__main__":
    main()
