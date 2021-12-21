import numpy as np


def main():

    n = float(input("Square root of which number?"))  #user input
    initial_number = 1
    i = 1
    error = abs(initial_number - np.sqrt(n)) / abs(np.sqrt(n))  #error formula

    while error >= (10**-15):  #always continues while error is greater than 10**-15
        x = initial_number - ((initial_number**2) - n) / (2*initial_number)   #finds first iteration
        error = abs(initial_number - np.sqrt(n)) / abs(np.sqrt(n))   #updates error
        initial_number = x   #sets initial number as x for next iteration
        print(i, x)
        i = i + 1

if __name__ == "__main__":
    main()