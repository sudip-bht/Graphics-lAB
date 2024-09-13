import glfw
from OpenGL.GL import *
from sutherland_hodegman_polygonClipping import sutherland_hodgman_clip
x_min = -0.5
y_min = -0.5
x_max = 0.5
y_max = 0.5
clip_window = [(x_min, y_min), (x_max, y_min), (x_max, y_max), (x_min, y_max)]
polygon = [(0.01,0.2),(0.1,0.5),(0.4,0.7),(0.4,0.3),(0.2,0.1)]
def draw_polygon(polygon):
    glBegin(GL_LINE_LOOP)
    for vertex in polygon:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(10.0)
    glColor3f(0.0, 0.0, 0.0)
    draw_polygon(clip_window)
    glColor3f(0.0, 0.0, 1.0)
    draw_polygon(polygon)
    clipped_polygon = sutherland_hodgman_clip(polygon,x_min,y_min,x_max,y_max)
    if clipped_polygon:
        glColor3f(1.0, 0.0, 0.0)
        draw_polygon(clipped_polygon)
    
    glFlush()

def main():
    if not glfw.init():
        return
    window = glfw.create_window(1200, 1200, "Sutherland-Hodgman Clipping", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glOrtho(-1, 1, -1, 1, 0, 1)
    while not glfw.window_should_close(window):
        draw()
        glfw.swap_buffers(window)
        glfw.poll_events()
    glfw.terminate()

if __name__ == "__main__":
    main()
