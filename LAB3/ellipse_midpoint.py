from draw_opengl import drawShape
def drawEllipse(x_center,y_center,r_x,r_y):
    points=[]
    x=0
    y=r_y
    r_x_2=pow(r_x,2)
    r_y_2=pow(r_y,2)
    p1=r_y_2-r_x_2*r_y+(1/4*r_x_2)
    while 2*r_y_2*x<2*r_x_2*y:
        points.extend(calculateSymmetricPoints(x,y,x_center,y_center))
        if p1<0:
            x=x+1
            p1=p1+2*r_y_2*x+r_y_2
        else:
            x=x+1
            y=y-1
            p1=p1+2*r_y_2*x-2*r_x_2*y+r_y_2
    p2=r_y_2*(pow((x+1/2),2))+r_x_2*pow((y-1),2)-r_x_2*r_y_2
    while y>=0:
        points.extend(calculateSymmetricPoints(x,y,x_center,y_center))
        if p2<0:
            x=x+1
            y=y-1
            p2=p2+2*r_y_2*x-2*r_x_2*y+r_x_2
        else:
            y=y-1
            p2=p2-2*r_x_2*y+r_x_2
    return points
def calculateSymmetricPoints(x,y,x_center,y_center):
    symmetric_coordinates = [
        (x + x_center, y + y_center), (-x + x_center, y + y_center),
        (-x + x_center, -y + y_center), (x + x_center, -y + y_center)
    ]
    return symmetric_coordinates

def main():
    all_points=drawEllipse(100,100,400,200)
    drawShape(all_points,"Mid Point Ellipse Drawing Algorithm")
 
    

if __name__ == "__main__":
    main()