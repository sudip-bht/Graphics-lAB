import glfw
from OpenGL.GL import *
from math import cos, sin, sqrt, pi




#colors associated with logo
blue = [0.529, 0.808, 0.922, 1.0]
yellow = [1.0, 1.0, 0.0, 1.0]
black = [0.0, 0.0, 0.0, 1.0]
red = [1.0, 0.0, 0.0, 1.0]
light_pink = [1.0, 0.714, 0.757, 1.0]
white=[1.0,1.0,1.0,1.0]



#fix center for circle
x_center=600
y_center=600


#draws circle
def draw_circle(x_cordinate, y_cordinate, radius, segment, color):
    glBegin(GL_POLYGON) 
    glColor4fv(color)
    for i in range(segment):
        theta = 2.0 * pi * i / segment
        x = radius * cos(theta) + x_cordinate
        y = radius * sin(theta) + y_cordinate
        glVertex2f(x, y)
    glEnd()

#divider line
def divider_lines(x_coordinate, y_coordinate, radius, num_segments):
    glLineWidth(8.0)
    glBegin(GL_LINES)
    glColor4fv(black)
    delta_theta = 2.0 * pi / num_segments
    for i in range(num_segments):
        theta = delta_theta * i
        x1 = x_coordinate
        y1 = y_coordinate
        x2 = radius* cos(theta) + x_coordinate
        y2 = radius * sin(theta) + y_coordinate
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
    glEnd()


def red_polygon(x_coordinate, y_coordinate, radius, segments):
    #for drawing black line outside the polygon
    glLineWidth(12.0)
    glBegin(GL_LINES)
    glColor4fv(black)
    delta_theta = 2.0 * pi / segments
    for i in range(segments):
        theta1 = delta_theta * i
        theta2 = delta_theta * (i + 1)
        x1 = radius * cos(theta1) + x_coordinate
        y1 = radius * sin(theta1) + y_coordinate
        x2 = radius * cos(theta2) + x_coordinate
        y2 = radius * sin(theta2) + y_coordinate

        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
    glEnd()

    #for filling the polygon with red color
    glBegin(GL_POLYGON) 
    glColor4fv(red)
    delta_theta = 2.0 * pi / segments
    for i in range(segments):
        theta1 = delta_theta * i
        theta2 = delta_theta * (i + 1)
        x1 = radius * cos(theta1) + x_coordinate
        y1 = radius * sin(theta1) + y_coordinate
        x2 = radius * cos(theta2) + x_coordinate
        y2 = radius * sin(theta2) + y_coordinate

        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
    glEnd()

def upsidedown_traingle(x, y, radius, color):
    glLineWidth(8.0)
    x1,y1=x,y+radius
    x2,y2=x-radius*sqrt(3) / 2,y - radius / 2
    x3,y3=x+radius*sqrt(3) / 2,y - radius / 2
    glColor4fv(black)
    glBegin(GL_LINE_LOOP)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()

    glBegin(GL_POLYGON)
    glColor4fv(color)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()


def traingle(cx, cy, r_outer, r_inner, color):
    glLineWidth(4.0) 
    glColor4fv(black) 
    glBegin(GL_LINE_LOOP) 
    x1_outer, y1_outer, x2_outer, y2_outer, x3_outer, y3_outer = cx, cy - r_outer, cx - r_outer * sqrt(3) / 2, cy + r_outer / 2, cx + r_outer * sqrt(3) / 2, cy + r_outer / 2
    glVertex2f(x1_outer, y1_outer)
    glVertex2f(x2_outer, y2_outer)
    glVertex2f(x3_outer, y3_outer)
    glEnd()

    glColor4fv(black)  
    glBegin(GL_LINE_LOOP)
    x1_inner, y1_inner, x2_inner, y2_inner, x3_inner, y3_inner = cx, cy - r_inner, cx - r_inner * sqrt(3) / 2, cy + r_inner / 2, cx + r_inner * sqrt(3) / 2, cy + r_inner / 2
    glVertex2f(x1_inner, y1_inner)
    glVertex2f(x2_inner, y2_inner)
    glVertex2f(x3_inner, y3_inner)
    glEnd()


#for filling white colors
    glColor4fv(white)  
    glBegin(GL_QUADS) 
    glVertex2f(x1_inner, y1_inner)
    glVertex2f(x2_inner, y2_inner)
    glVertex2f(x2_outer, y2_outer)
    glVertex2f(x1_outer, y1_outer)
    glEnd()

    glBegin(GL_QUADS) 
    glVertex2f(x2_inner, y2_inner)
    glVertex2f(x3_inner, y3_inner)
    glVertex2f(x3_outer, y3_outer)
    glVertex2f(x2_outer, y2_outer)
    glEnd()

    glBegin(GL_QUADS)  
    glVertex2f(x3_inner, y3_inner)
    glVertex2f(x1_inner, y1_inner)
    glVertex2f(x1_outer, y1_outer)
    glVertex2f(x3_outer, y3_outer)
    glEnd()
   

    

def draw_rectangle(x, y, width, height):
    glColor4fv(black)  
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()



def draw_u_shape(x, y, width, height, space, rotation):
    pivot_x = x
    pivot_y = y
    glTranslatef(pivot_x, pivot_y, 0)
    glRotatef(rotation, 0, 0, 1)
    glTranslatef(-pivot_x, -pivot_y, 0)
    
    glColor4fv(black)
    
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x, y + height + 20)
    glVertex2f(x+width,y + height + 20)
    glVertex2f(x+width, y)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(x+width,y+height)
    glVertex(x+width+space,y+height)
    glVertex(x+width+space,y+height+20)
    glVertex2f(x+width,y+height+20)
    glEnd()

    glBegin(GL_QUADS)
    glVertex(x+width+space,y+height+20)
    glVertex(x+2*width+space,y+height+20)
    glVertex(x+2*width+space,y)
    glVertex(x+width+space,y)
    glEnd()
    


def main():
    if not glfw.init():
        print("Failed to initialize GLFW")
        return -1

    window = glfw.create_window(1000, 1000, "KU-LOGO", None, None)
    if not window:
        glfw.terminate()
        return -1

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, x_center*2 ,y_center*2, 0, 0, 1)
        glColor3f(1.0, 1.0, 1.0)
    
        red_polygon(x_center,y_center,360,12)
        divider_lines(x_center,y_center,360,12)
        draw_circle(x_center,y_center, 300, 360, black)
        draw_circle(x_center,y_center, 290, 360, blue)
        draw_circle(x_center,y_center, 230, 100, black)
        draw_circle(x_center,y_center, 220, 100, yellow)
        upsidedown_traingle(x_center,y_center,220,light_pink)
        traingle(x_center,y_center, 225, 185, white)
        draw_circle(x_center,375,30, 200,white)
        draw_circle(x_center-220* sqrt(3) / 2,y_center+220/2,30, 360,white)
        draw_circle(x_center+220* sqrt(3) / 2,y_center+220/2,30, 200,white)
        draw_rectangle(x=540,y=525,width=20,height=135)
        draw_u_shape(x=605,y=525,width=20,height=80,space=50,rotation=30)
       
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
