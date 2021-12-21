import numpy as np
import matplotlib.pyplot as plt

def main():
    name = input("Enter compressed coordinate matrix file name:")
    load = np.loadtxt(name)

    line = load[:, 0]   #all in 0
    column = load[:, 1]   #all in 1
    color = load[:, 2]   #all in 2
    x = int(np.max(line))   #finds max
    y = int(np.max(column))   #finds max

    image = np.zeros((x + 1, y + 1))   #new array with zeros
    for i in range(len(line)):
        image[int(line[i]), int(column[i])] = color[i]   #sets equal to the color
    plt.imshow(image, cmap="binary")
    plt.show()

if __name__ == "__main__":
    main()