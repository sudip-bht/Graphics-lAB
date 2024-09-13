import glfw
from OpenGL.GL import *

X_BASE = 500
Y_BASE = 500

def drawTraingle(old_points, new_points, label, pointsize=5):
    if not glfw.init():
        print("Failed to initialize GLFW")
        return -1
    
    window = glfw.create_window(1000, 1000, label, None, None)
    if not window:
        glfw.terminate()
        return -1
    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0,1200,0,1200, 0, 1)
        
        # Draw old triangle in blue
        glColor4fv([0.0, 0.0, 1.0, 1.0]) 
        glPointSize(pointsize) 
        glBegin(GL_TRIANGLES)
        for point in old_points:
            
            glVertex2f(point[0] + X_BASE, point[1] + Y_BASE)
        glEnd()
        
        # Draw new triangle in red
        glColor4fv([1.0, 0.0, 0.0, 1.0]) 
        glPointSize(pointsize) 
        glBegin(GL_TRIANGLES)
        for point in new_points:
            
            glVertex2f(point[0] + X_BASE, point[1] + Y_BASE)
        glEnd()
        
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

