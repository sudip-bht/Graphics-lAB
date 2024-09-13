from plotpoints import plot
from draw_histogram import generate_histogram
from draw_line import plot_line
def DDA(x_start ,y_start,x_end,y_end):
    x=x_start
    y=y_start
    dx=x_end-x_start
    dy=y_end-y_start
    if(abs(dx)>abs(dy)):
        stepsize=abs(dx)
    else:
        stepsize=abs(dy)
        
    x_inc=dx/stepsize
    y_inc=dy/stepsize


    points = []
    for i in range(stepsize):
        points.append((x, y))
        x=x+x_inc
        y=y+y_inc
    points.append((x_end,y_end))

    return points

def main():
    x_start = int(input("Enter the x-coordinate of the starting point(integer): "))
    y_start = int(input("Enter the y-coordinate of the starting point(integer): "))
    x_end = int(input("Enter the x-coordinate of the ending point(integer): "))
    y_end = int(input("Enter the y-coordinate of the ending point(integer): "))
    #DDA LINE DRAWING
    all_points=DDA(x_start=x_start,y_start=y_start,x_end=x_end,y_end=y_end)
    all_x_coordinates=[point[0] for point in all_points]
    all_y_coordinates=[point[1] for point in all_points]

    plot(all_x_coordinates,all_y_coordinates,'DDA Line Drawing Alogrithm')
    plot_line(x_start,y_start,y_start,y_end,DDA,"DDA")

    #DDA histogram
    histogram_data = [20, 30, 75, 100, 50, 45, 95]
    generate_histogram(histogram_data,DDA,"DDA")

if __name__ == "__main__":
    main()


