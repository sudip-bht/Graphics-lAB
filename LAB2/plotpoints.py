import matplotlib.pyplot as plt
def plot(x_coordinates,y_coordinates,label):
    
    plt.title(label)
    plt.plot(x_coordinates, y_coordinates, marker='o')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    
    plt.show()
    


if __name__ == "__main__":
    plot()