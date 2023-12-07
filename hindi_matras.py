import numpy as np
import math
from matplotlib import pyplot as plt

le = np.e
pe = math.pi
t = np.arange(0,1,0.001)


# name = 'final_font/m-आ'
# x_p1 = 7.5 + 4*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 2 + 8*t

# name = 'final_font/m-viram'
# x_p1 = 9 + 0*t
# y_p1 = 2 + 8*t

# name = 'final_font/m-अः'
# x_p1 = 11 + 0.5*np.cos(0 + (2*pe)*t)
# y_p1 = 7.5 + 0.5*np.sin(0 + (2*pe)*t)

# x_p2 = 11 + 0.5*np.cos(0 + (2*pe)*t)
# y_p2 = 4.5 + 0.5*np.sin(0 + (2*pe)*t)


# name = 'final_font/m-ऋ'
# x_p1 = 12.55 + 1.25*np.cos(5*pe/8 + (pe)*t)
# y_p1 = 4.4 + 1.25*np.sin(5*pe/8 + (pe)*t)


# name = 'final_font/m-ओ'
# x_p1 = 7.5 + 4*t
# y_p1 = 10 + 0*t

# x_p2 = 10 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 6.5 + 3.5*t
# y_p3 = 13.5 - 3.5*t


# name = 'final_font/m-औ'
# x_p1 = 7.5 + 4*t
# y_p1 = 10 + 0*t

# x_p2 = 10 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 6.5 + 3.5*t
# y_p3 = 13.5 - 3.5*t

# x_p4 = 7 + 3*t
# y_p4 = 14 - 4*t


# name = 'final_font/m-ए'
# x_p1 = 7.5 + 4*t
# y_p1 = 10 + 0*t

# x_p2 = 6.5 + 3.5*t
# y_p2 = 13.5 - 3.5*t


# name = 'final_font/m-ऐ'
# x_p1 = 7.5 + 4*t
# y_p1 = 10 + 0*t

# x_p2 = 6.5 + 3.5*t
# y_p2 = 13.5 - 3.5*t

# x_p3 = 7 + 3*t
# y_p3 = 14 - 4*t


# name = 'final_font/m-इ'
# x_p1 = 7.5 + 4*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 9 + 2.5*np.cos(1.5 + (pe)*t)
# y_p3 = 10.8 + 0.8*np.sin(1.5 + (pe)*t)

# x_p4 = 9 + 6.0*np.cos(0 + (pe/2)*t)
# y_p4 = 10.8 + 0.8*np.sin(0 + (pe/2)*t)


# name = 'final_font/m-ई'
# x_p1 = 7.5 + 4*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 9 + 2.5*np.cos(-1.5 + (pe)*t)
# y_p3 = 10.8 + 0.8*np.sin(-1.5 + (pe)*t)

# x_p4 = 9 + 4.5*np.cos(pe/2 + (pe/2)*t)
# y_p4 = 10.8 + 0.8*np.sin(pe/2 + (pe/2)*t)



# name = 'final_font/m-उ'
# x_p1 = 9 + 0.5*np.cos((-pe/2) + (pe+pe/3)*t)
# y_p1 = 1 + 0.5*np.sin((-pe/2) + (pe+pe/3)*t)

# x_p2 = 9 + 2*np.cos(pe + (3*pe/5-0.28)*t)
# y_p2 = 1 + 0.5*np.sin(pe + (3*pe/5-0.28)*t)


# name = 'final_font/m-ऊ'
# x_p1 = 9 + 0.5*np.cos(pe/4 + (6*pe/4)*t)
# y_p1 = -0.5 + 0.5*np.sin(pe/4 + (6*pe/4)*t)

# x_p2 = 9 + 0.5*np.cos(pe/4) + 2*t
# y_p2 = -0.5 + 0.5*np.sin(pe/4) - 2*t


# name = 'final_font/m-अं'
# x_p1 = 7.5 + 3*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0.5*np.cos(0 + (2*pe)*t)
# y_p2 = 12 + 0.5*np.sin(0 + (2*pe)*t)

# name = 'final_font/m-Halant'
# x_p1 = 7 + 3*t
# y_p1 = 14 - 3*t

graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1, y_p1, 'k', linewidth=5.0)
# out.plot(x_p2, y_p2, 'k', linewidth=5.0)
# out.plot(x_p3, y_p3, 'k', linewidth=5.0)
# out.plot(x_p4, y_p4, 'k', linewidth=5.0)
# out.plot(x_p5, y_p5, 'k', linewidth=5.0)
# out.plot(x_p6, y_p6, 'k', linewidth=5.0)
# out.plot(x_p7, y_p7, 'k', linewidth=5.0)
# out.plot(x_p8, y_p8, 'k', linewidth=5.0)
out.axis('off')
plt.show()