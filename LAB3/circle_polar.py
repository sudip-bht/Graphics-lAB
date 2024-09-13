import numpy as np
from draw_opengl import drawShape
def drawCircle(x_center,y_center,radius):
    points=[]
    x=0
    y=radius
    step_size=1/radius;
    theta_end=np.pi/4;
    theta=0;
    
    while theta<theta_end:
        points.extend(calculateSymmetricPoints(x,y,x_center,y_center))
        x=radius*np.cos(theta)
        y=radius*np.sin(theta)
        theta+=step_size
    return points;

def calculateSymmetricPoints(x,y,x_center,y_center):
    symmetric_coordinates = [
        (x + x_center, y + y_center), (y + x_center, x + y_center),
        (-y + x_center, x + y_center), (-x + x_center, y + y_center),
        (-x + x_center, -y + y_center), (-y + x_center, -x + y_center),
        (y + x_center, -x + y_center), (x + x_center, -y + y_center)
    ]
    return symmetric_coordinates

def main():
    all_points=drawCircle(100,100,300)
    drawShape(all_points,"Polar Circle Drawing Algorithm")
if __name__ == "__main__":
    main()





