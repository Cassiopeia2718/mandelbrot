import numpy as np
from matplotlib import pyplot as plt
import math

def mandelbrot(minX, maxX, minY, maxY, widthPixels, iterations, fileName):

    pixelDensity = (maxX - minX)/widthPixels

    a = np.arange(minX, maxX + pixelDensity, pixelDensity)
    b = np.arange(minY, maxY + pixelDensity, pixelDensity)

    A = np.tile(a, (len(b), 1))
    B = np.ndarray.transpose(np.tile(b, (len(a), 1)))

    Plane = np.empty(np.shape(A), dtype=np.complex128)

    Plane.real = A
    Plane.imag = B

    mandelbrot = np.sqrt(isStable(plane, iterations))

    plt.imshow(mandelbrot)
    plt.imsave(file_name + ".png", mandelbrot)
    plt.show()
     
def isStable(z, iterations):

    z_new = np.zeros(np.shape(z))
    z_color = np.zeros(np.shape(z)) 
    i = 0

    while i < iterations:

        z_new = np.square(z_new) + z
        z_color[np.where(np.square(np.real(z_new)) + np.square(np.imag(z_new)) >= 2)] = i
        z_new[np.where(np.square(np.real(z_new)) + np.square(np.imag(z_new))  >= 2)] = None
        print(i)
        i+=1

        if i == iterations:

            plt.imshow(z_color)
            plt.show()

            if input("Are you satisfid(yes/no): ") == "no":
                iterations += int(input("Number of iterations more(int): "))

    return z_color

mandelbrot(-1.5, 0.5, -1, 1, 20000, 25, "Mandelbrot")
