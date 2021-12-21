import numpy as np
import matplotlib.pyplot as plt


def main():



    a = input("Enter (x,y) of  point-1, default is (0.5,0.5):")   #enters value
    if a == "":
        x1, y1 = 0.5, 0.5
    else:
        b = a.split(",")   #splits input
        x1 = float(b[0])
        y1 = float(b[1])

    c = input("Enter (x,y) of  point-2, default is (3,2.5):")   #enters value
    if c == "":
        x2 = 3
        y2 = 2.5
    else:
        d = c.split(",")  #splits input
        x2 = float(d[0])
        y2 = float(d[1])

    e = input("Enter (x,y) of  point-3, default is (1,3):")   #enters value
    if e == "":
        x3 = 1
        y3 = 3
    else:
        f = e.split(",")  #splits input
        x3 = float(f[0])
        y3 = float(f[1])

    ymin = min(y1, y2, y3)   #finds min
    ymax = max(y1, y2, y3)   #finds max
    xmin = min(x1, x2, x3)   #finds min
    xmax = max(x1, x2, x3)   #finds max

    np.random.seed(7)
    n = 100000
    x = np.random.uniform(xmin, xmax, n)   #generates 100000 random x values
    y = np.random.uniform(ymin, ymax, n)   #generates 100000 random y values

    counter = 0
    total_area = np.empty(n)
    domain = (ymax - ymin) * (xmax - xmin)   #domain equal to ymax-ymin * xmax-xmin
    array = np.array([[x1, x2, x3], [y1, y2, y3], [1, 1, 1]])   # creates 3D array

    for i in range(n):
        coords = np.array([[x[i]], [y[i]], [1]])   #creates array
        a_array = np.linalg.solve(array, coords)   #performs linear algebra
        multiply = array.dot(coords)

        a1 = a_array[0]
        a2 = a_array[1]
        a3 = a_array[2]

        if a1 > 0 and a2 > 0 and a3 > 0:
            counter = counter + 1
            total_area[i] = (domain / float(i + 1) * counter)
        else:
            total_area[i] = (domain / float(i + 1) * counter)   #area of the triangle

    print("Using 10 samples, area of the triangle is " + str(total_area[10 - 1]))   #print statement for all n values
    print("Using 100 samples, area of the triangle is " + str(total_area[100 - 1]))
    print("Using 1000 samples, area of the triangle is " + str(total_area[1000 - 1]))
    print("Using 10000 samples, area of the triangle is " + str(total_area[10000 - 1]))
    print("Using 100000 samples, area of the triangle is " + str(total_area[100000 - 1]))

    plt.figure(1)   #creates figure one
    t = np.arange(0, 10**5)  #uses values 10**5
    plt.plot(t, total_area[t])   #plots t values for area
    plt.xscale("log")   #uses log scale
    plt.ylim(-0.2, 3)   #sets y axis range
    plt.xlabel("Area-Triangle")
    plt.ylabel("#samples")

    xt = np.array([x1, x2, x3, x1])   #creates loop of x points
    yt = np.array([y1, y2, y3, y1])   #creates loop of y points

    plt.figure(2)   #creates figure two
    plt.subplot(2, 2, 1)   #four graphs on figure two
    plt.plot(xt, yt)   #creates triangle
    plt.scatter(x[:10], y[:10], color="r")   #for values up to 10
    plt.xticks([])
    plt.yticks([])
    plt.title("n="+str(10)+", area= %.3f" % (total_area[10-1]))

    plt.subplot(2, 2, 2)
    plt.plot(xt, yt)   #creates triangle
    plt.scatter(x[:100], y[:100], color="r")   #for values up to 100
    plt.xticks([])
    plt.yticks([])
    plt.title("n="+str(100)+", area= %.3f" % (total_area[100-1]))

    plt.subplot(2, 2, 3)
    plt.plot(xt, yt)   #creates triangle
    plt.scatter(x[:1000], y[:1000], color="r")   #for values up to 1000
    plt.xticks([])
    plt.yticks([])
    plt.title("n="+str(1000)+", area= %.3f" % (total_area[1000-1]))

    plt.subplot(2, 2, 4)
    plt.plot(xt, yt)   #creates triangle
    plt.scatter(x[:10000], y[:10000], color="r")   #for values up to 10000
    plt.xticks([])
    plt.yticks([])
    plt.title("n="+str(10000)+", area= %.3f" % (total_area[10000-1]))

    plt.show()

if __name__=="__main__":
    main()


