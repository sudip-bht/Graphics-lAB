INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8   

def assign_regioncode(x,y,x_min,y_min,x_max,y_max):
    code = INSIDE
    if x < x_min:      # to the left of rectangle
        code |= LEFT
    elif x > x_max:    # to the right of rectangle
        code |= RIGHT
    if y < y_min:      # below the rectangle
        code |= BOTTOM
    elif y > y_max:    # above the rectangle
        code |= TOP
    return code

