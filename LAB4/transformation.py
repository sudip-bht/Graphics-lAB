import numpy as np
from transfromationMatrices import TwoDTransformations
from draw_traingle import drawTraingle

def main():
    transform = TwoDTransformations()
    
    print("Enter the coordinates of the triangle:")
    first_coordinates = input("First Coordinate (X,Y): ")
    second_coordinates = input("Second Coordinate (X,Y): ")
    third_coordinates = input("Third Coordinate (X,Y): ")    
    
    coordinates_list = [first_coordinates, second_coordinates, third_coordinates]
    
    print("\nChoose the type of transformation:")
    print("1. Translation")
    print("2. Rotation")
    print("3. Reflection")
    print("4. Shearing")
    print("5. Scaling")
    print("6. Composite")
    
    transformationOption = input("Enter your choice (1-6): ")
    
    transformmatrix = np.identity(3)
    new_coordinates = []
    old_coordinates = []
    
    match transformationOption:
        case '1':
            tx = float(input("Enter the translation distance for x-axis: "))
            ty = float(input("Enter the translation distance for y-axis: "))
            transformmatrix = np.dot(transformmatrix, transform.twoDTranslation(tx, ty))
        case '2':
            angle = float(input("Enter the rotation angle (in degrees): "))
            transformmatrix = np.dot(transformmatrix, transform.twoDRotation(angle))
        case '3':
            axis = input("Enter the axis of reflection (x, y, y=x, origin): ")
            match axis:
                case 'x':
                    transformmatrix = np.dot(transformmatrix, transform.twoDReflectionXAxis())
                case 'y':
                    transformmatrix = np.dot(transformmatrix, transform.twoDReflectionYAxis())
                case 'y=x':
                    transformmatrix = np.dot(transformmatrix, transform.twoDReflectionYEqualX())
                case 'origin':
                    transformmatrix = np.dot(transformmatrix, transform.twoDReflectionAboutOrigin())
                case _:
                    print("Invalid axis for reflection.")
        case '4':
            axis=input("Enter the axis of shearing (x, y): ")
            match axis:
                case 'x':
                    shx = input("Enter the shearing factor for x-axis: ")
                    transformmatrix = np.dot(transformmatrix, transform.twoDShearingXaxis(float(shx)))
                case 'y':
                    shy = float(input("Enter the shearing factor for y-axis: "))
                    transformmatrix = np.dot(transformmatrix, transform.twoDShearingYaxis(shy)) 
                case _:
                    print("Invalid axis for Shearing.")
        case '5':
            sx = float(input("Enter the scaling factor for x-axis: "))
            sy = float(input("Enter the scaling factor for y-axis: "))
            transformmatrix = np.dot(transformmatrix, transform.twoDScaling(sx, sy))
        case '6':
            while True:
                sub_option = input("Choose a transformation for composite:\n1. Translation\n2. Rotation\n3. Reflection\n4. Shearing\n5. Scaling\n6. None\nEnter your choice (1-6): ")
                match sub_option:
                    case '1':
                        tx = float(input("Enter the translation distance for x-axis: "))
                        ty = float(input("Enter the translation distance for y-axis: "))
                        transformmatrix = np.dot(transformmatrix, transform.twoDTranslation(tx, ty))
                    case '2':
                        angle = float(input("Enter the rotation angle (in degrees): "))
                        transformmatrix = np.dot(transformmatrix, transform.twoDRotation(angle))
                    case '3':
                        axis = input("Enter the axis of reflection (x, y, y=x, origin): ")
                        match axis:
                            case 'x':
                                transformmatrix = np.dot(transformmatrix, transform.twoDReflectionXAxis())
                            case 'y':
                                transformmatrix = np.dot(transformmatrix, transform.twoDReflectionYAxis())
                            case 'y=x':
                                transformmatrix = np.dot(transformmatrix, transform.twoDReflectionYEqualX())
                            case 'origin':
                                transformmatrix = np.dot(transformmatrix, transform.twoDReflectionAboutOrigin())
                            case _:
                                print("Invalid axis for reflection.")
                    case '4':
        
                        axis=input("Enter the axis of shearing (x, y): ")
                        match axis:
                            case 'x':
                                shx = input("Enter the shearing factor for x-axis: ")
                                transformmatrix = np.dot(transformmatrix, transform.twoDShearingXaxis(float(shx)))
                            case 'y':
                                shy = float(input("Enter the shearing factor for y-axis: "))
                                transformmatrix = np.dot(transformmatrix, transform.twoDShearingYaxis(shy)) 
                            case _:
                                print("Invalid axis for Shearing.")        
                    case '5':
                        sx = float(input("Enter the scaling factor for x-axis: "))
                        sy = float(input("Enter the scaling factor for y-axis: "))
                        transformmatrix = np.dot(transformmatrix, transform.twoDScaling(sx, sy))
                    case '6':
                        break
                    case _:
                        print("Invalid option, please try again.")
    
    for coord in coordinates_list:
        x, y = map(float, coord.split(','))
        old_coordinates.append((x, y))
        old_point = np.array([x, y, 1])
        new_point = np.dot(transformmatrix, old_point)
        new_point = np.squeeze(np.asarray(new_point))
        new_coordinates.append((new_point[0], new_point[1]))
    
    drawTraingle(old_points=old_coordinates, new_points=new_coordinates, label="Transformation")

if __name__ == "__main__":
    main()
