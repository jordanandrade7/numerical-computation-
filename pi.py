##################################################
###### IF YOU WORK BY GROUP OF TWO ###############
###### ENTER YOUR TWO NAMES HERE:  ###############
###### Name1=Jordan Andrade
###### Name2=
######
###### Only 1 submission on moodle (either names ok)
##################################################

import numpy as np
import matplotlib.pyplot as plt
import math


def main():

    np.random.seed(5)
    n=1000000
    xy = np.random.uniform(-1, 1, (2, n))   #generate random x y values
    x = xy[0, :]   #first row are the x values
    y = xy[1, :]   #second row are the y values
    d = (x**2+y**2)
    pi_list = []   #intialize the list
    counter = 0

    for i in range(n):   #monte carlo integration for loop
        if d[i] <= 1:
            counter = counter+1   #keeps count
        v = (4/(i+1))*counter
        pi_list.append(v)   #appends the value to the list
    pi = np.array(pi_list)   #creates an array of the final values

    print("Using " + str(10) + " samples, pi is " + str(pi[10 - 1]))   # print statements for given n values
    print("Using " + str(100) + " samples, pi is " + str(pi[100 - 1]))
    print("Using " + str(1000) + " samples, pi is " + str(pi[1000 - 1]))
    print("Using " + str(10000) + " samples, pi is " + str(pi[10000 - 1]))
    print("Using " + str(100000) + " samples, pi is " + str(pi[100000 - 1]))
    print("Using " + str(1000000) + " samples, pi is " + str(pi[1000000 - 1]))


    plt.figure(1)   #creates figure 1
    t=np.arange(0, 10**6)   #goes all the way up to 10**6
    plt.plot(t, pi[t])   #plots pi of 10**6
    plt.xscale("log")   #uses log values for x axis
    plt.ylim(1.5, 4)   #sets y limit
    plt.xlabel("pi")
    plt.ylabel("#samples")

    plt.figure(2)   #creates second figure
    plt.subplot(2, 2, 1)   #allows four plots on 1 figure
    r = 1
    theta = np.arange(0, 2 * np.pi, np.pi / 180)
    a = np.cos(theta)
    b = np.sin(theta)
    plt.plot(r * a, r * b)   #creates circle with radius of 1
    plt.scatter(x[:10], y[:10], color="r")   #for value up to 10
    plt.xticks([])
    plt.yticks([])
    plt.title("n="+str(10)+", pi= %.3f" % (pi[10-1]))   #puts to the accuracy of 3

    plt.subplot(2, 2, 2)
    plt.plot(r * a, r * b)   #creates circle
    plt.scatter(x[:100], y[:100], color="r")   #up to 100
    plt.xticks([])
    plt.yticks([])
    plt.title("n="+str(100)+", pi= %.3f" % (pi[100-1]))

    plt.subplot(2, 2, 3)
    plt.plot(r * a, r * b)   #creates circle
    plt.scatter(x[:1000], y[:1000], color="r")   #up to 1000
    plt.xticks([])
    plt.yticks([])
    plt.title("n="+str(1000)+", pi= %.3f" % (pi[1000-1]))

    plt.subplot(2, 2, 4)
    plt.plot(r * a, r * b)   #creates circle
    plt.scatter(x[:10000], y[:10000], color="r")   #up to 10000
    plt.xticks([])
    plt.yticks([])
    plt.title("n="+str(10000)+", pi= %.3f" % (pi[10000-1]))

    plt.show()

if __name__=="__main__":
    main()
