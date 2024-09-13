import glfw
import math
from OpenGL.GL import *
COLOR = [
    [0.529, 0.808, 0.922, 1.0],  # Light blue
    [1.0, 1.0, 0.0, 1.0],         # Yellow
    [0.0, 0.0, 0.0, 1.0],         # Black
    [1.0, 0.0, 0.0, 1.0],         # Red
    [1.0, 0.714, 0.757, 1.0],     # Light pink
    [0.0, 1.0, 0.0, 1.0],         # Green
    [0.5, 0.5, 0.5, 1.0],         # Gray
    [0.678, 0.847, 0.902, 1.0],  # Light blue (alternate shade)
    [0.863, 0.863, 0.863, 1.0],   # Light gray
]

def plot_histogram(histogram_data, algorithm, bar_width=100, base_x=300, base_y=700):
    max_value = max(histogram_data)
    min_value = min(histogram_data)
    
    # Draw axes
    glLineWidth(4.0)
    glColor4fv(COLOR[2]) 
    glBegin(GL_LINES)
    # y-axis
    glVertex2f(base_x-2, base_y)
    glVertex2f(base_x-2, base_y - max_value * math.floor(max_value / min_value) - 10)  
    # x-axis
    glVertex2f(base_x-2, base_y)
    glVertex2f(base_x + (len(histogram_data)) * bar_width + 10, base_y)  
    glEnd()

    for i, height in enumerate(histogram_data):
        x1 = base_x + i * bar_width
        y1 = base_y
        x2 = x1 + bar_width
        y2 = base_y - height * math.floor(max_value / min_value)  #calculates height factor 
        points = algorithm(x1, y1, x1, y2) + algorithm(x1, y2, x2, y2) + algorithm(x2, y2, x2, y1) + algorithm(x2, y1, x1, y1)
        glColor4fv(COLOR[i])  
        glBegin(GL_POLYGON)
        for point in points:
            glVertex2f(point[0], point[1])
        glEnd()

def generate_histogram(histogram_data,algorithm ,label):
    if not glfw.init():
        print("Failed to initialize GLFW")
        return -1

    window = glfw.create_window(1000, 1000, "HISTORGRAM USING "+label, None, None)
    if not window:
        glfw.terminate()
        return -1
    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, 1200 ,0, 1200, 0, 1)
        glColor3f(1.0, 1.0, 1.0)
        plot_histogram(histogram_data,algorithm)
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()