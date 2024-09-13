def inside(p, edge,x_min,y_min,x_max,y_max):
    if edge == 'LEFT':
        return p[0] >= x_min
    elif edge == 'RIGHT':
        return p[0] <= x_max
    elif edge == 'BOTTOM':
        return p[1] >= y_min
    elif edge == 'TOP':
        return p[1] <= y_max

def intersect(p1, p2, edge,x_min,y_min,x_max,y_max):
    if edge == 'LEFT':
        x = x_min
        y = p1[1] + (p2[1] - p1[1]) * (x_min - p1[0]) / (p2[0] - p1[0])
    elif edge == 'RIGHT':
        x = x_max
        y = p1[1] + (p2[1] - p1[1]) * (x_max - p1[0]) / (p2[0] - p1[0])
    elif edge == 'BOTTOM':
        y = y_min
        x = p1[0] + (p2[0] - p1[0]) * (y_min - p1[1]) / (p2[1] - p1[1])
    elif edge == 'TOP':
        y = y_max
        x = p1[0] + (p2[0] - p1[0]) * (y_max - p1[1]) / (p2[1] - p1[1])
    return (x, y)

def sutherland_hodgman_clip(polygon,x_min,y_min,x_max,y_max ):
    clipped_polygon = polygon
    for edge in ['LEFT', 'RIGHT', 'BOTTOM', 'TOP']:
        new_polygon = []
        for i in range(len(clipped_polygon)):
            p1 = clipped_polygon[i]
            p2 = clipped_polygon[(i + 1) % len(clipped_polygon)]
            if inside(p2, edge,x_min,y_min,x_max,y_max ):
                if not inside(p1, edge,x_min,y_min,x_max,y_max ):
                    new_polygon.append(intersect(p1, p2, edge,x_min,y_min,x_max,y_max ))
                new_polygon.append(p2)
            elif inside(p1, edge,x_min,y_min,x_max,y_max):
                new_polygon.append(intersect(p1, p2, edge,x_min,y_min,x_max,y_max ))
        clipped_polygon = new_polygon

    return clipped_polygon
if __name__ == "__main__":
    polygon = [(50, 150), (200, 50), (350, 150), (350, 300), (250, 300), (200, 250), (150, 350), (100, 250)]
    sutherland_hodgman_clip(polygon,0,0,200,200)