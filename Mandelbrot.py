import numpy as np
from matplotlib import pyplot as plt
import math

def mandelbrot(min_X, max_X, min_Y, max_Y, width_pixels, itterations, file_name):

    pixel_density = (max_X - min_X)/width_pixels

    a = np.arange(min_X, max_X + pixel_density, pixel_density)
    b = np.arange(min_Y, max_Y + pixel_density, pixel_density)

    A = np.tile(a, (len(b), 1))
    B = np.ndarray.transpose(np.tile(b, (len(a), 1)))

    Plane = np.empty(np.shape(A), dtype=np.complex128)

    Plane.real = A
    Plane.imag = B

    Mandelbrot = np.sqrt(isStable(Plane, itterations))

    plt.imshow(Mandelbrot)
    plt.imsave("/Users/nicholas/Desktop/Fractels/" + file_name + ".png", Mandelbrot)
    plt.show()
     
def isStable(z, itterations):

    z_new = np.zeros(np.shape(z))
    z_color = np.zeros(np.shape(z)) 
    i = 0

    while i < itterations:

        z_new = np.square(z_new) + z
        z_color[np.where(np.square(np.real(z_new)) + np.square(np.imag(z_new)) >= 2)] = i
        z_new[np.where(np.square(np.real(z_new)) + np.square(np.imag(z_new))  >= 2)] = None
        print(i)
        i+=1

        if i == itterations:

            plt.imshow(z_color)
            plt.show()

            if input("Are you satisfid(yes/no): ") == "no":
                itterations += int(input("Number of itterations more(int): "))

    return z_color

mandelbrot(-1.5, 0.5, -1, 1, 20000, 25, "Mandelbrot")