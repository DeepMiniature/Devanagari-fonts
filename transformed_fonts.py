import numpy as np
import math
from matplotlib import pyplot as plt

le = np.e
pe = math.pi

t = np.arange(0,1,0.001)

#Enter letter equation here
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

#transforms add as and when required
# 1. For the transformation f(z) = 1/z, add the following tranforms for each line
# u_1 = x_p1/(x_p1*x_p1 + y_p1*y_p1)
# v_1 = y_p1/(x_p1*x_p1 + y_p1*y_p1)

# u_2 = x_p2/(x_p2*x_p2 + y_p2*y_p2)
# v_2 = y_p2/(x_p2*x_p2 + y_p2*y_p2)

# u_3 = x_p3/(x_p3*x_p3 + y_p3*y_p3)
# v_3 = y_p3/(x_p3*x_p3 + y_p3*y_p3)

# u_4 = x_p4/(x_p4*x_p4 + y_p4*y_p4)
# v_4 = y_p4/(x_p4*x_p4 + y_p4*y_p4)

# u_5 = x_p5/(x_p5*x_p5 + y_p5*y_p5)
# v_5 = y_p5/(x_p5*x_p5 + y_p5*y_p5)


# 2. For the transformation f(z) = e^z, add the following transforms for each line
# u_1 = (le**x_p1)*np.cos(y_p1)
# v_1 = (le**x_p1)*np.sin(y_p1)

# u_2 = (le**x_p2)*np.cos(y_p2)
# v_2 = (le**x_p2)*np.sin(y_p2)

# u_3 = (le**x_p3)*np.cos(y_p3)
# v_3 = (le**x_p3)*np.sin(y_p3)

# u_4 = (le**x_p4)*np.cos(y_p4)
# v_4 = (le**x_p4)*np.sin(y_p4)

# u_5 = (le**x_p5)*np.cos(y_p5)
# v_5 = (le**x_p5)*np.sin(y_p5)


# 3. For the transformation f(z) = log(z), add the following transforms for each line
# u_1 = np.log((x_p1**2 + y_p1**2)**0.5)
# v_1 = np.arctan(y_p1/x_p1)

# u_2 = np.log((x_p2**2 + y_p2**2)**0.5)
# v_2 = np.arctan(y_p2/x_p2)

# u_3 = np.log((x_p3**2 + y_p3**2)**0.5)
# v_3 = np.arctan(y_p3/x_p3)

# u_4 = np.log((x_p4**2 + y_p4**2)**0.5)
# v_4 = np.arctan(y_p4/x_p4)

# u_5 = np.log((x_p5**2 + y_p5**2)**0.5)
# v_5 = np.arctan(y_p5/x_p5)


# 4. For the transformation f(z) = sin(z), add the following transforms for each line
# u_1 = np.sin(x_p1)*np.cosh(y_p1)
# v_1 = np.cos(x_p1)*np.sinh(y_p1)

# u_2 = np.sin(x_p2)*np.cosh(y_p2)
# v_2 = np.cos(x_p2)*np.sinh(y_p2)

# u_3 = np.sin(x_p3)*np.cosh(y_p3)
# v_3 = np.cos(x_p3)*np.sinh(y_p3)

# u_4 = np.sin(x_p4)*np.cosh(y_p4)
# v_4 = np.cos(x_p4)*np.sinh(y_p4)

# u_5 = np.sin(x_p5)*np.cosh(y_p5)
# v_5 = np.cos(x_p5)*np.sinh(y_p5)


# 5. For the transformation f(z) = z^c, add  the following transforms for each line
# c = 2

# u_1 = ((x_p1**2 + y_p1**2)**(0.5*c))*np.cos(c*np.arctan(y_p1/x_p1))
# v_1 = ((x_p1**2 + y_p1**2)**(0.5*c))*np.sin(c*np.arctan(y_p1/x_p1)) 

# u_2 = ((x_p2**2 + y_p2**2)**(0.5*c))*np.cos(c*np.arctan(y_p2/x_p2))
# v_2 = ((x_p2**2 + y_p2**2)**(0.5*c))*np.sin(c*np.arctan(y_p2/x_p2)) 

# u_3 = ((x_p3**2 + y_p3**2)**(0.5*c))*np.cos(c*np.arctan(y_p3/x_p3))
# v_3 = ((x_p3**2 + y_p3**2)**(0.5*c))*np.sin(c*np.arctan(y_p3/x_p3)) 

# u_4 = ((x_p4**2 + y_p4**2)**(0.5*c))*np.cos(c*np.arctan(y_p4/x_p4))
# v_4 = ((x_p4**2 + y_p4**2)**(0.5*c))*np.sin(c*np.arctan(y_p4/x_p4)) 

# u_5 = ((x_p5**2 + y_p5**2)**(0.5*c))*np.cos(c*np.arctan(y_p5/x_p5))
# v_5 = ((x_p5**2 + y_p5**2)**(0.5*c))*np.sin(c*np.arctan(y_p5/x_p5)) 


# 6. Inverse Exponential Function (e^(1/z))
# u_1 = np.exp(x_p1 / (x_p1**2 + y_p1**2)) * np.cos(-y_p1 / (x_p1**2 + y_p1**2))
# v_1 = np.exp(x_p1 / (x_p1**2 + y_p1**2)) * np.sin(-y_p1 / (x_p1**2 + y_p1**2))

# u_2 = np.exp(x_p2 / (x_p2**2 + y_p2**2)) * np.cos(-y_p2 / (x_p2**2 + y_p2**2))
# v_2 = np.exp(x_p2 / (x_p2**2 + y_p2**2)) * np.sin(-y_p2 / (x_p2**2 + y_p2**2))

# u_3 = np.exp(x_p3 / (x_p3**2 + y_p3**2)) * np.cos(-y_p3 / (x_p3**2 + y_p3**2))
# v_3 = np.exp(x_p3 / (x_p3**2 + y_p3**2)) * np.sin(-y_p3 / (x_p3**2 + y_p3**2))

# u_4 = np.exp(x_p4 / (x_p4**2 + y_p4**2)) * np.cos(-y_p4 / (x_p4**2 + y_p4**2))
# v_4 = np.exp(x_p4 / (x_p4**2 + y_p4**2)) * np.sin(-y_p4 / (x_p4**2 + y_p4**2))

# u_5 = np.exp(x_p5 / (x_p5**2 + y_p5**2)) * np.cos(-y_p5 / (x_p5**2 + y_p5**2))
# v_5 = np.exp(x_p5 / (x_p5**2 + y_p5**2)) * np.sin(-y_p5 / (x_p5**2 + y_p5**2))


#7. Tan Function
# u(t) = sin(2x) / (cos(2x) + cosh(2y))
# v(t) = sinh(2y) / (cos(2x) + cosh(2y))

u_1 = np.sin(2*x_p1) / ((np.cos(2*x_p1)) + (np.cosh(2*y_p1)))
v_1 = np.sinh(2*y_p1) / ((np.cos(2*x_p1)) + (np.cosh(2*y_p1)))

u_2 = np.sin(2*x_p2) / ((np.cos(2*x_p2)) + (np.cosh(2*y_p2)))
v_2 = np.sinh(2*y_p2) / ((np.cos(2*x_p2)) + (np.cosh(2*y_p2)))

u_3 = np.sin(2*x_p3) / ((np.cos(2*x_p3)) + (np.cosh(2*y_p3)))
v_3 = np.sinh(2*y_p3) / ((np.cos(2*x_p3)) + (np.cosh(2*y_p3)))

u_4 = np.sin(2*x_p4) / ((np.cos(2*x_p4)) + (np.cosh(2*y_p4)))
v_4 = np.sinh(2*y_p4) / ((np.cos(2*x_p4)) + (np.cosh(2*y_p4)))

u_5 = np.sin(2*x_p5) / ((np.cos(2*x_p5)) + (np.cosh(2*y_p5)))
v_5 = np.sinh(2*y_p5) / ((np.cos(2*x_p5)) + (np.cosh(2*y_p5)))

# just add new out.plot statements as and when required
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
out.plot(u_1,v_1,'k')
out.plot(u_2,v_2,'k')
out.plot(u_3,v_3,'k')
out.plot(u_4,v_4,'k')
out.plot(u_5,v_5,'k')
# plt.xlim(0,10.5)
# plt.ylim(0,10)
out.axis('off')
plt.show()