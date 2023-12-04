import numpy as np
import math
from matplotlib import pyplot as plt

le = np.e
pe = math.pi

t = np.arange(0,1,0.001)

#A
# x_p1 = 1 + t
# y_p1 = 3*t

# x_p2 = 2 + t
# y_p2 = 3 - 3*t

# x_p3 = 1.5 + t
# y_p3 = 1.5 + 0*t

# graph = plt.figure()
# out = graph.add_subplot(1,1,1)
# out.set_aspect('equal')
# out.plot(x_p1,y_p1,'k')
# out.plot(x_p2,y_p2,'k')
# out.plot(x_p3,y_p3,'k')
# out.axis('off')
# plt.show()

#D
x_p1 = 3 + np.cos(3*pe/2 + (pe)*t)
y_p1 = 2 + np.sin(3*pe/2 + (pe)*t)

x_p2 = 2.5 + 0*t
y_p2 = 1 + 2*t

x_p3 = 2.5 + 0.5*t
y_p3 = 3 + 0*t

x_p4 = 2.5 + 0.5*t
y_p4 = 1 + 0*t

graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(x_p1,y_p1,'k')
out.plot(x_p2,y_p2,'k')
out.plot(x_p3,y_p3,'k')
out.plot(x_p4,y_p4,'k')
out.axis('off')
plt.show()