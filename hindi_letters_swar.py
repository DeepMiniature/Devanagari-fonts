import numpy as np
import math
from matplotlib import pyplot as plt

le = np.e
pe = math.pi
t = np.arange(0,1,0.001)

#अ
x_p1 = 7.5 + 3*t
y_p1 = 10 + 0*t

x_p2 = 9 + 0*t
y_p2 = 2 + 8*t

x_p3 = 6 + 3*t
y_p3 = 6.5 + 0*t

x_p4 = 6 + 1.75*np.cos(3*pe/2 + (5*pe/4)*t)
y_p4 = 8.25 + 1.75*np.sin(3*pe/2 + (5*pe/4)*t)

x_p5 = 6 + 2.25*np.cos(5*pe/4 + (5*pe/4)*t)
y_p5 = 4.25 + 2.25*np.sin(5*pe/4 + (5*pe/4)*t)

#आ
# x_p1 = 7.5 + 4*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 6 + 3*t
# y_p3 = 6.5 + 0*t

# x_p4 = 10 + 0*t
# y_p4 = 2 + 8*t

# x_p5 = 6 + 1.75*np.cos(3*pe/2 + (5*pe/4)*t)
# y_p5 = 8.25 + 1.75*np.sin(3*pe/2 + (5*pe/4)*t)

# x_p6 = 6 + 2.25*np.cos(5*pe/4 + (5*pe/4)*t)
# y_p6 = 4.25 + 2.25*np.sin(5*pe/4 + (5*pe/4)*t)

#इ
# x_p1 = 7.5 + 3*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 8 + 2*t

# x_p3 = 9 + 2.25*np.cos(pe/2 + (pe)*t)
# y_p3 = 5.75 + 2.25*np.sin(pe/2 + (pe)*t)

# x_p4 = 9 + 2.25*np.cos(3*pe/2 + (pe)*t)
# y_p4 = 1.25 + 2.25*np.sin(3*pe/2 + (pe)*t)

# x_p5 = 9 + 0.5*np.cos(pe/4 + (5*pe/4)*t)
# y_p5 = -0.5 + 0.5*np.sin(pe/4 + (5*pe/4)*t)

# x_p6 = 9 + 0.5*np.cos(pe/4) + 2*t
# y_p6 = -0.5 + 0.5*np.sin(pe/4) - 2*t

#ई
# x_p1 = 7.5 + 3*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 8 + 2*t

# x_p3 = 9 + 2.25*np.cos(pe/2 + (pe)*t)
# y_p3 = 5.75 + 2.25*np.sin(pe/2 + (pe)*t)

# x_p4 = 9 + 2.25*np.cos(3*pe/2 + (pe)*t)
# y_p4 = 1.25 + 2.25*np.sin(3*pe/2 + (pe)*t)

# x_p5 = 9 + 0.5*np.cos(pe/4 + (5*pe/4)*t)
# y_p5 = -0.5 + 0.5*np.sin(pe/4 + (5*pe/4)*t)

# x_p6 = 9 + 0.5*np.cos(pe/4) + 2*t
# y_p6 = -0.5 + 0.5*np.sin(pe/4) - 2*t

# x_p7 = 9 + 1.5*np.cos(pe/4 + (5*pe/4)*t)
# y_p7 = 11.5 + 1.5*np.sin(pe/4 + (5*pe/4)*t)

# उ
# x_p1 = 6 + 4.5*t
# y_p1 = 10 + 0*t

# x_p2 = 8 + 1.75*np.cos(3*pe/2 + (15*pe/16)*t)
# y_p2 = 8.25 + 1.75*np.sin(3*pe/2 + (15*pe/16)*t)

# x_p3 = 8 + 2.25*np.cos(5*pe/4 + (5*pe/4)*t)
# y_p3 = 4.25 + 2.25*np.sin(5*pe/4 + (5*pe/4)*t)

#ऊ
# x_p1 = 6 + 4.5*t
# y_p1 = 10 + 0*t

# x_p2 = 8 + 1.75*np.cos(3*pe/2 + (15*pe/16)*t)
# y_p2 = 8.25 + 1.75*np.sin(3*pe/2 + (15*pe/16)*t)

# x_p3 = 8 + 2.25*np.cos(5*pe/4 + (5*pe/4)*t)
# y_p3 = 4.25 + 2.25*np.sin(5*pe/4 + (5*pe/4)*t)

# x_p4 = 10.4 + 1.5*np.cos(7*pe/4 + (9*pe/8)*t)
# y_p4 = 5.7 + 1.5*np.sin(7*pe/4 + (9*pe/8)*t)

#ऋ
# x_p1 = 7 + 5*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 6.5 + 2.5*t
# y_p3 = 8 - 2*t

# x_p4 = 6.5 + 2.5*t
# y_p4 = 4 + 2*t

# x_p5 = 9 + 2.45*t
# y_p5 = 6 + 1*t

# x_p6 = 11.3 + 0.3*np.cos((3*pe)/2 + (7*pe/4)*t)
# y_p6 = 7.25 + 0.3*np.sin((3*pe)/2 + (7*pe/4)*t)

# x_p7 = 11.3 + 0.3*np.cos((13*pe)/4) + 1*t
# y_p7 = 7.25 + 0.3*np.sin((13*pe)/4) - 1.5*t

# x_p8 = 12.55 + 1.25*np.cos(5*pe/8 + (pe)*t)
# y_p8 = 4.4 + 1.25*np.sin(5*pe/8 + (pe)*t)

#ए
# x_p1 = 6 + 5*t
# y_p1 = 10 + 0*t

# x_p2 = 7 + 0*t
# y_p2 = 6 + 4*t

# x_p3 = 10 + 0*t
# y_p3 = 6 + 4*t

# x_p4 = 7 + 3.5*t
# y_p4 = 6 - 3.5*t

# x_p5 = 10 - 1.5*t
# y_p5 = 6 - 0.5*t

#ऐ
# x_p1 = 6 + 5*t
# y_p1 = 10 + 0*t

# x_p2 = 7 + 0*t
# y_p2 = 6 + 4*t

# x_p3 = 10 + 0*t
# y_p3 = 6 + 4*t

# x_p4 = 7 + 3.5*t
# y_p4 = 6 - 3.5*t

# x_p5 = 10 - 1.5*t
# y_p5 = 6 - 0.5*t

# x_p6 = 6.5 + 3.5*t
# y_p6 = 13.5 - 3.5*t

#ओ
# x_p1 = 7.5 + 4*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 6 + 3*t
# y_p3 = 6.5 + 0*t

# x_p4 = 10 + 0*t
# y_p4 = 2 + 8*t

# x_p5 = 6 + 1.75*np.cos(3*pe/2 + (5*pe/4)*t)
# y_p5 = 8.25 + 1.75*np.sin(3*pe/2 + (5*pe/4)*t)

# x_p6 = 6 + 2.25*np.cos(5*pe/4 + (5*pe/4)*t)
# y_p6 = 4.25 + 2.25*np.sin(5*pe/4 + (5*pe/4)*t)

# x_p7 = 6.5 + 3.5*t
# y_p7 = 13.5 - 3.5*t

#औ
# x_p1 = 7.5 + 4*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 6 + 3*t
# y_p3 = 6.5 + 0*t

# x_p4 = 10 + 0*t
# y_p4 = 2 + 8*t

# x_p5 = 6 + 1.75*np.cos(3*pe/2 + (5*pe/4)*t)
# y_p5 = 8.25 + 1.75*np.sin(3*pe/2 + (5*pe/4)*t)

# x_p6 = 6 + 2.25*np.cos(5*pe/4 + (5*pe/4)*t)
# y_p6 = 4.25 + 2.25*np.sin(5*pe/4 + (5*pe/4)*t)

# x_p7 = 6.5 + 3.5*t
# y_p7 = 13.5 - 3.5*t

# x_p8 = 7 + 3*t
# y_p8 = 14 - 4*t

#अं
# x_p1 = 7.5 + 3*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 6 + 3*t
# y_p3 = 6.5 + 0*t

# x_p4 = 6 + 1.75*np.cos(3*pe/2 + (5*pe/4)*t)
# y_p4 = 8.25 + 1.75*np.sin(3*pe/2 + (5*pe/4)*t)

# x_p5 = 6 + 2.25*np.cos(5*pe/4 + (5*pe/4)*t)
# y_p5 = 4.25 + 2.25*np.sin(5*pe/4 + (5*pe/4)*t)

# x_p6 = 9 + 0.5*np.cos(0 + (2*pe)*t)
# y_p6 = 12 + 0.5*np.sin(0 + (2*pe)*t)

#अः
# x_p1 = 7.5 + 3*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 6 + 3*t
# y_p3 = 6.5 + 0*t

# x_p4 = 6 + 1.75*np.cos(3*pe/2 + (5*pe/4)*t)
# y_p4 = 8.25 + 1.75*np.sin(3*pe/2 + (5*pe/4)*t)

# x_p5 = 6 + 2.25*np.cos(5*pe/4 + (5*pe/4)*t)
# y_p5 = 4.25 + 2.25*np.sin(5*pe/4 + (5*pe/4)*t)

# x_p6 = 11 + 0.5*np.cos(0 + (2*pe)*t)
# y_p6 = 7.5 + 0.5*np.sin(0 + (2*pe)*t)

# x_p7 = 11 + 0.5*np.cos(0 + (2*pe)*t)
# y_p7 = 4.5 + 0.5*np.sin(0 + (2*pe)*t)

graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1, y_p1, 'k', linewidth=5.0)
out.plot(x_p2, y_p2, 'k', linewidth=5.0)
out.plot(x_p3, y_p3, 'k', linewidth=5.0)
out.plot(x_p4, y_p4, 'k', linewidth=5.0)
out.plot(x_p5, y_p5, 'k', linewidth=5.0)
# out.plot(x_p6,y_p6,'k')
# out.plot(x_p7,y_p7,'k')
# out.plot(x_p8,y_p8,'k')
out.axis('off')
plt.show()