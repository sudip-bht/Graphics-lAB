import glfw
from OpenGL.GL import *
from cohen_sutherland_lineclipping import cohen_sutherland_clip
x_min=400
y_min=200
x_max=800
y_max=600
x1, y1 = 350, 210
x2, y2 = 750, 650
def draw_line(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()
def draw_rect(x_min, y_min, x_max, y_max):
    glBegin(GL_LINE_LOOP)
    glVertex2f(x_min, y_min)
    glVertex2f(x_max, y_min)
    glVertex2f(x_max, y_max)
    glVertex2f(x_min, y_max)
    glEnd()
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(10.0)
    draw_rect(x_min, y_min, x_max, y_max)
    glColor3f(0.0, 0.0, 1.0)
    draw_line(x1, y1, x2, y2)
    
    # Perform Cohen-Sutherland clipping
    clipped_line = cohen_sutherland_clip(x1, y1, x2, y2,x_min,y_min,x_max,y_max)
  
    if clipped_line:
        glColor3f(1.0, 0.0, 0.0)
        draw_line(*clipped_line)
    glFlush()

def main():
    
    if not glfw.init():
        return
    window = glfw.create_window(1200, 1200, "Cohen-Sutherland Clipping", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glOrtho(0, 1200, 0, 1200,0,1)
    while not glfw.window_should_close(window):
        draw()
        glfw.swap_buffers(window)
        glfw.poll_events()
    
    glfw.terminate()

if __name__ == "__main__":
    main()