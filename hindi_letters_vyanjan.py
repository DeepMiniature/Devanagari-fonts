import numpy as np
import math
from matplotlib import pyplot as plt

le = np.e
pe = math.pi

t = np.arange(0,1,0.001)

# क
# x_p1 = 6 + 6*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 7.25 + 1.75*np.cos(0 + (2*pe)*t)
# y_p3 = 6 + 1.75*np.sin(0 + (2*pe)*t)

# x_p4 = 10.75 + 1.75*np.cos(6*pe/4 + (6*pe/4)*t)
# y_p4 = 6 + 1.75*np.sin(6*pe/4 + (6*pe/4)*t)


# ख
# x_p1 = 1 + 11*t
# y_p1 = 10 + 0*t

# x_p2 = 9.2 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 7.3 + 1.75*np.cos(0 + (2*pe)*t)
# y_p3 = 6 + 1.75*np.sin(0 + (2*pe)*t)

# x_p4 = 3 + 2.25*np.cos(3*pe/2 + (pe)*t)
# y_p4 = 7.75 + 2.25*np.sin(3*pe/2 + (pe)*t)

# x_p5 = 3 + 0.5*np.cos(pe/4 + (5*pe/4)*t)
# y_p5 = 6 + 0.5*np.sin(pe/4 + (5*pe/4)*t)

# x_p6 = 3 + 0.5*np.cos(pe/4) + 3.2*t
# y_p6 = 6 + 0.5*np.sin(pe/4)- 3.2*t

# x_p7 = 8 + 2*np.cos((pe+0.6) + pe/2*t)
# y_p7 = 4.5 + 2*np.sin((pe+0.6) + pe/2*t)

# ग
# x_p1 = 5 + 6*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 7 + 0*t
# y_p3 = 4 + 6*t

# x_p4 = 6.5 + 0.5*np.cos(2*pe*t)
# y_p4 = 4 + 0.5*np.sin(2*pe*t)


#gha
# x_p1 = 3 + 7*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 6 + 2.25*np.cos(5*pe/6 + (4*pe/6)*t)
# y_p3 = 8.8 + 2.25*np.sin(5*pe/6 + (4*pe/6)*t)

# x_p4 = 6 + 1.75*np.cos(pe/2 + (7*pe/6)*t)
# y_p4 = 4.75 + 1.75*np.sin(pe/2 + (7*pe/6)*t)

# x_p5 = 6 + 1.75*np.cos(pe/2 + (7*pe/6)) + 2*t
# y_p5 = 4.75 + 1.75*np.sin(pe/2 + (7*pe/6)) + 1*t

# च
# x_p1 = 5 + 6*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 6.013 + 1.6*t
# y_p3 = 7.237 + 0*t

# x_p4 = 7.25 + 1.75*np.cos((3*pe/4) + (5*pe/4)*t)
# y_p4 = 6 + 1.75*np.sin((3*pe/4) + (5*pe/4)*t)

# x_p5 = 6.013 - 2*t
# y_p5 = 7.237 + 0*t

# न
# x_p1 = 5 + 6*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 6 + 0*t
# y_p3 = 5 + 2*t

# x_p4 = 6 - 2*t
# y_p4 = 5 + 2*t

# x_p5 = 4 + 5*t
# y_p5 = 7 + 0*t

# ब
# x_p1 = 5 + 6*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 7.25 + 1.75*np.cos(0 + (2*pe)*t)
# y_p3 = 6 + 1.75*np.sin(0 + (2*pe)*t)

# x_p4 = 7.25 + 1.25*t
# y_p4 = 6 + 1.25*t

# x_p5 = 7.25 - 1.25*t
# y_p5 = 6 - 1.25*t

# म
# x_p1 = 5 + 6*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 6 + 0*t
# y_p3 = 3 + 7*t

# x_p4 = 6 - 2*t
# y_p4 = 3 + 2*t

# x_p5 = 4 + 5*t
# y_p5 = 5 + 0*t

# र
# x_p1 = 7.5 + 5*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 2.25*np.cos(3*pe/2 + (pe)*t)
# y_p2 = 7.75 + 2.25*np.sin(3*pe/2 + (pe)*t)

# x_p3 = 9 + 0.5*np.cos(pe/4 + (5*pe/4)*t)
# y_p3 = 6 + 0.5*np.sin(pe/4 + (5*pe/4)*t)

# x_p4 = 9 + 0.5*np.cos(pe/4) + 4.5*t
# y_p4 = 6 + 0.5*np.sin(pe/4)- 4.5*t

# व
# x_p1 = 5 + 6*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 7.25 + 1.75*np.cos(0 + (2*pe)*t)
# y_p3 = 6 + 1.75*np.sin(0 + (2*pe)*t)




graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
try:
    out.plot(x_p1, y_p1, 'k', linewidth=5.0)
    out.plot(x_p2, y_p2, 'k', linewidth=5.0)
    out.plot(x_p3, y_p3, 'k', linewidth=5.0)
    out.plot(x_p4, y_p4, 'k', linewidth=5.0)
    out.plot(x_p5, y_p5, 'k', linewidth=5.0)
    out.plot(x_p6, y_p6, 'k', linewidth=5.0)
    out.plot(x_p7, y_p7, 'k', linewidth=5.0)
    out.plot(x_p8, y_p8, 'k', linewidth=5.0)
    out.plot(x_p9, y_p9, 'k', linewidth=5.0)
except:
    pass
out.axis('off')
# plt.savefig('plot_image.png')
plt.show()