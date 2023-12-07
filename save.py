import numpy as np
import math
from matplotlib import pyplot as plt

le = np.e
pe = math.pi

t = np.arange(0,1,0.001)

#Enter letter equation here
#अ
name = "enter name here"

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

# 5. For the transformation f(z) = z^c, add  the following transforms for each line
c = 2

try:
    u_1 = ((x_p1**2 + y_p1**2)**(0.5*c))*np.cos(c*np.arctan(y_p1/x_p1))
    v_1 = ((x_p1**2 + y_p1**2)**(0.5*c))*np.sin(c*np.arctan(y_p1/x_p1)) 

    u_2 = ((x_p2**2 + y_p2**2)**(0.5*c))*np.cos(c*np.arctan(y_p2/x_p2))
    v_2 = ((x_p2**2 + y_p2**2)**(0.5*c))*np.sin(c*np.arctan(y_p2/x_p2)) 

    u_3 = ((x_p3**2 + y_p3**2)**(0.5*c))*np.cos(c*np.arctan(y_p3/x_p3))
    v_3 = ((x_p3**2 + y_p3**2)**(0.5*c))*np.sin(c*np.arctan(y_p3/x_p3)) 

    u_4 = ((x_p4**2 + y_p4**2)**(0.5*c))*np.cos(c*np.arctan(y_p4/x_p4))
    v_4 = ((x_p4**2 + y_p4**2)**(0.5*c))*np.sin(c*np.arctan(y_p4/x_p4)) 

    u_5 = ((x_p5**2 + y_p5**2)**(0.5*c))*np.cos(c*np.arctan(y_p5/x_p5))
    v_5 = ((x_p5**2 + y_p5**2)**(0.5*c))*np.sin(c*np.arctan(y_p5/x_p5)) 

    u_6 = ((x_p6**2 + y_p6**2)**(0.5*c))*np.cos(c*np.arctan(y_p6/x_p6))
    v_6 = ((x_p6**2 + y_p6**2)**(0.5*c))*np.sin(c*np.arctan(y_p6/x_p6)) 

    u_7 = ((x_p7**2 + y_p7**2)**(0.5*c))*np.cos(c*np.arctan(y_p7/x_p7))
    v_7 = ((x_p7**2 + y_p7**2)**(0.5*c))*np.sin(c*np.arctan(y_p7/x_p7)) 

    u_8 = ((x_p8**2 + y_p8**2)**(0.5*c))*np.cos(c*np.arctan(y_p8/x_p8))
    v_8 = ((x_p8**2 + y_p8**2)**(0.5*c))*np.sin(c*np.arctan(y_p8/x_p8)) 

    u_9 = ((x_p9**2 + y_p9**2)**(0.5*c))*np.cos(c*np.arctan(y_p9/x_p9))
    v_9 = ((x_p9**2 + y_p9**2)**(0.5*c))*np.sin(c*np.arctan(y_p9/x_p9)) 

    u_10 = ((x_p10**2 + y_p10**2)**(0.5*c))*np.cos(c*np.arctan(y_p10/x_p10))
    v_10 = ((x_p10**2 + y_p10**2)**(0.5*c))*np.sin(c*np.arctan(y_p10/x_p10)) 

except:
    pass

# just add new out.plot statements as and when required
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
try:
    out.plot(u_1, v_1, 'k', linewidth=5.0)
    out.plot(u_2, v_2, 'k', linewidth=5.0)
    out.plot(u_3, v_3, 'k', linewidth=5.0)
    out.plot(u_4, v_4, 'k', linewidth=5.0)
    out.plot(u_5, v_5, 'k', linewidth=5.0)
    out.plot(u_6, v_6, 'k', linewidth=5.0)
    out.plot(u_7, v_7, 'k', linewidth=5.0)
    out.plot(u_8, v_8, 'k', linewidth=5.0)
    out.plot(u_9, v_9, 'k', linewidth=5.0)
    out.plot(u_10, v_10, 'k', linewidth=5.0)
except:
    pass
out.axis('off')
plt.savefig(name)
plt.show()