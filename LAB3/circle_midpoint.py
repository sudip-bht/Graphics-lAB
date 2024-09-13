from draw_opengl import drawShape
def drawCircle(radius,x_center,y_center):
    x=0;
    points=[] 
    y=radius;
    p=1-radius;
    while x<y: 
        points.extend(calculateSymmetricPoints(x,y,x_center,y_center))
        if(p<0):
            x=x+1;
            p=p+2*x+1;
        else :
            x=x+1;
            y=y-1;
            p=p+2*x+1-2*y
    return points

def calculateSymmetricPoints(x,y,x_center,y_center):
    symmetric_coordinates = [
        (x + x_center, y + y_center), (y + x_center, x + y_center),
        (-y + x_center, x + y_center), (-x + x_center, y + y_center),
        (-x + x_center, -y + y_center), (-y + x_center, -x + y_center),
        (y + x_center, -x + y_center), (x + x_center, -y + y_center)
    ]
    return symmetric_coordinates



def main():
    all_points=drawCircle(300,100,50)
    drawShape(all_points,"Mid Point Circle Drawing Algorithm")
 
    

if __name__ == "__main__":
    main()









  
        
   
    



