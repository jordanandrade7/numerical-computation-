import numpy as np
import matplotlib.pyplot as plt

def main():

    a = input("Newton fractal z ** n = 1, Enter n (default 3):")  #user input
    if a == "":   #default values
        n = 3
    else:
        n = int(a)

    b = input("Enter xmin, xmax, ymin, ymax (default -1.35, 1.35, -1.35, 1.35):")   #user input
    if b == "":   #default values
        xmin, xmax, ymin, ymax = -1.35, 1.35, -1.35, 1.35
    else:
        c = b.split(",")   #splits input
        xmin = float(c[0])
        xmax = float(c[1])
        ymin = float(c[2])
        ymax = float(c[3])

    solution = []   #intialize list
    for i in range(n):   #appends to the list
        solution = solution + [np.exp((1j*2*np.pi*i) / n)]

    print(str(solution), end="\n")

    x = np.linspace(xmin+0.00011, xmax, 1000)   #generates 1000 points
    y = np.linspace(ymin+0.00011, ymax, 1000)   #generate 1000 points

    C = np.zeros((1000, 1000), dtype=complex)   #creates matrix

    for i in range(1000):   #generates 1000x1000
        for j in range(1000):
            C[i, j] = x[j] + 1j * y[i]   #calculating values of C

    for i in range(20):   #20 iterations
        C = C - (C / n) + (1 / n) * (1 /C)**(n - 1)

    colors = np.zeros((1000, 1000), dtype=int)

    for i in range(1000):   #getting shape for root solutions
        for j in range(1000):
            index = -1
            low = float('inf')
            val = C[i, j]
            for m in range(len(solution)):
                error = abs(val - solution[m]) / abs(solution[m])   #finds error
                if error < low:   #finds the value with the smallest error
                    low = error
                    index = m
            colors[i, j] = (index * 225) / (n -1)

    plt.imshow(colors, cmap="rainbow", interpolation="bilinear", origin="lower", extent=[xmin, xmax, ymin, ymax])   #plots
    plt.show()


if __name__ == "__main__":
    main()