import numpy as np
import math
from matplotlib import pyplot as plt

le = np.e
pe = math.pi
t = np.arange(0,1,0.001)

# name = 'final_font/0'
# x_p1 = 3 + 1*np.cos(0 + (2*pe)*t)
# y_p1 = 3 + 1*np.sin(0 + (2*pe)*t)


# name = 'final_font/1'
# x_p1 = 5 + 0.5*np.cos(0 + 2*pe*t)
# y_p1 = 10 + 0.5*np.sin(0 + 2*pe*t)

# x_p2 = 5 + 0.8*np.cos((-pe/2 - 0.4) + (pe)*t)
# y_p2 = 9.38 + 1.1*np.sin((-pe/2 - 0.4)  + (pe)*t)

# x_p3 = 4.35 + 0.5*np.cos(pe/4) + 1.3*t
# y_p3 = 8 + 0.5*np.sin(pe/4) - 1.7*t

# name = 'final_font/2'
# x_p1 = 6 + 1*np.cos((3*pe/2) + (5*pe/4-0.55)*t)
# y_p1 = 7.95 + 1.2*np.sin((3*pe/2) + (5*pe/4-0.55)*t)

# x_p2 = 6 + 0.3*np.cos(0.7 + (2*pe-2.2)*t)
# y_p2 = 7.05 + 0.3*np.sin(0.7 + (2*pe-2.2)*t)

# x_p3 = 5.92 + 0.5*np.cos(pe/4+0.1) + 1.3*t
# y_p3 = 6.85 + 0.5*np.sin(pe/4+0.1) - 1.7*t


# name = 'final_font/3'
# x_p1 = 6 + 1.75*np.cos(3*pe/2 + (5*pe/4)*t)
# y_p1 = 8.25 + 1.75*np.sin(3*pe/2 + (5*pe/4)*t)

# x_p2 = 6 + 2.25*np.cos(5*pe/4 + (5*pe/4)*t)
# y_p2 = 4.25 + 2.25*np.sin(5*pe/4 + (5*pe/4)*t)

# x_p3 = 4.85 + 0.5*np.cos((0.5) + (7*pe/6)*t)
# y_p3 = 2.9 + 0.5*np.sin((0.5) + (7*pe/6)*t)

# x_p4 = 5.28 + 0*t
# y_p4 = 0.65 + 2.5*t


# name = 'final_font/4'
# x_p1 = 6 + 1.5*np.cos(0 + (-pe)*t)
# y_p1 = 6 + 2.25*np.sin(0 + (-pe)*t)

# x_p2 = 6 + 0.5*np.cos(0 + (2*pe)*t)
# y_p2 = 3.15 + 0.6*np.sin(0 + (2*pe)*t)


# name = 'final_font/5'
# x_p1 = 6 + 1.5*np.cos(pe-0.7 + (pe+0.)*t)
# y_p1 = 6 + 2.25*np.sin(pe-0.7 + (pe+0.)*t)

# x_p2 = 7 + 0.2*np.cos(0 + (2*pe)*t)
# y_p2 = 4.75 + 0.3*np.sin(0 + (2*pe)*t)

# x_p3 = 6.57 + 0.5*np.cos(pe/4+0.1) + 1.*t
# y_p3 = 4.1 + 0.5*np.sin(pe/4+0.1) - 2.*t


# name = 'final_font/6'
# x_p1 = 6 + 1.75*np.cos(pe/2 + (4*pe/4)*t)
# y_p1 = 8.25 + 1.75*np.sin(pe/2 + (4*pe/4)*t)

# x_p2 = 6 + 2.25*np.cos(pe/2 + (5*pe/4)*t)
# y_p2 = 4.25 + 2.25*np.sin(pe/2 + (5*pe/4)*t)

# x_p3 = 7.15 + 0.5*np.cos((-0.5) + (7*pe/6)*t)
# y_p3 = 2.9 + 0.5*np.sin((-0.5) + (7*pe/6)*t)

# x_p4 = 6.63 + 0*t
# y_p4 = 0.4 + 2.5*t


# name = 'final_font/7'
# x_p1 = 6 + 1.5*np.cos(pe-0.7 + (pe+0.6)*t)
# y_p1 = 6 + 2.5*np.sin(pe-0.7 + (pe+0.6)*t)

# x_p2 = 7.04 + 0.45*np.cos(0 + (2*pe-1)*t)
# y_p2 = 5.75 + 0.6*np.sin(0 + (2*pe-1)*t)


# name = 'final_font/8'
# x_p1 = 6 + 1*np.cos(pe-0.2 + (pe+0.2)*t)
# y_p1 = 3 + 0.95*np.sin(pe-0.2 + (pe+0.2)*t)

# x_p2 = 5.7 + 0.5*np.cos(pe/4+0.1) - 1.*t
# y_p2 = 4.3 + 0.5*np.sin(pe/4+0.1) - 1.5*t


# name = 'final_font/9'
# x_p1 = 5 + 0.4*np.cos(-2 +(2*pe-.5)*t)
# y_p1 = 4 + 0.4*np.sin(-2 + (2*pe-.5)*t)

# x_p2 = 4.33 + 0.5*np.cos(pe/4) + 0.8*t
# y_p2 = 3.4 + 0.5*np.sin(pe/4) - 1.7*t

# x_p3 = 5.3 + 0.2*np.cos(-1.5 +(pe/2)*t)
# y_p3 = 2.0 + 0.2*np.sin(-1.5 + (pe/2)*t)




graph = plt.figure()
out = graph.add_subplot(1,1,1)
# plt.xlim(0, 20)
# plt.ylim(0, 20)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k', linewidth=5.0)
out.plot(x_p2,y_p2,'k', linewidth=5.0)
out.plot(x_p3,y_p3,'k', linewidth=5.0)
# out.plot(x_p4,y_p4,'k', linewidth=5.0)
out.axis('off')
plt.show()