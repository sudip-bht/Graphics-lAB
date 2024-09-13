import matplotlib.pyplot as plt
from plotpoints import plot
from draw_histogram import generate_histogram
from draw_line import plot_line
def BLA(x_start ,y_start,x_end,y_end):
    points=[]  #for storing the calculated points 
    dy=y_end-y_start
    dx=x_end-x_start

    #for checking if the points start from  right i.e end point is smaller then starting points
    if x_end >= x_start:
        sx = 1
    else:
        sx = -1
    if y_end >= y_start:
        sy = 1
    else:
        sy = -1
    x=x_start
    y=y_start
    if dx>dy:
        p=2*dy-dx   
    else:
        p=2*dx-dy


    if dx>dy:
        while x!=x_end:
            points.append((x,y))
            if p<0:
                y=y
                p=p+2*dy
            else:
                y=y+sy
                p=p+2*dy-2*dx
            x=x+sx
    else:
        while y!=y_end:
            points.append((x,y))
            if p<0:
                x=x
                p=p+2*dx
            else:
                x=x+1
                p=p+2*dx-2*dy
            y=y+sy
    points.append((x_end,y_end))
    return points

def main():
    x_start = int(input("Enter the x-coordinate of the starting point(integer): "))
    y_start = int(input("Enter the y-coordinate of the starting point(integer): "))
    x_end = int(input("Enter the x-coordinate of the ending point(integer): "))
    y_end = int(input("Enter the y-coordinate of the ending point(integer): "))

    #BLA LINE DRAWING GRID
    all_points=BLA(x_start=x_start,y_start=y_start,x_end=x_end,y_end=y_end)
    all_x_coordinates=[point[0] for point in all_points]
    all_y_coordinates=[point[1] for point in all_points]
    plot(all_x_coordinates,all_y_coordinates,'BLA Line Drawing Algorithm')
    plot_line(x_start=x_start,y_start=y_start,x_end=x_end,y_end=y_end,algorithm=BLA,label='BLA')
    

    #BLA Histogram
    histogram_data = [20, 30, 50, 100, 60, 75, 95]
    generate_histogram(histogram_data,BLA,"BLA")

 
if __name__ == "__main__":
    main()
  
        
   
    