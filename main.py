from numba import jit
import numpy
import matplotlib.pyplot as plt

@jit
def mandelbrot(Re, Im, max_iter):
    c = complex(Re, Im)
    z = 0.0j

    for i in range(max_iter):
        z = z*z + c
        if z.real * z.real + z.imag*z.imag >= 4:
            return i

    return max_iter


columns, rows = 2000, 2000
result = numpy.zeros((columns, rows))
for i, Re in enumerate(numpy.linspace(-2, 1, num=rows)):
    for j, Im in enumerate(numpy.linspace(-1, 1, num=columns)):
        result[i][j] = mandelbrot(Re, Im, 100)


plt.figure(dpi=100)
plt.imshow(result.T, cmap='inferno', interpolation='bilinear', extent=[-2, 1, -1, 1])
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()
