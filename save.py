import numpy as np
import math
from matplotlib import pyplot as plt

le = np.e
pe = math.pi
t = np.arange(0,1,0.001)

def rotate_points(u, v, angle_degrees):
    angle_rad = np.radians(angle_degrees)
    rotation_matrix = np.array([[np.cos(angle_rad), -np.sin(angle_rad)],
                                [np.sin(angle_rad), np.cos(angle_rad)]])
    rotated_points = np.dot(rotation_matrix, np.vstack((u, v)))
    return rotated_points[0], rotated_points[1]

# Insert the letter here




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

try:
    deg = 30
    ru_1, rv_1 = rotate_points(u_1, v_1, deg)
    ru_2, rv_2 = rotate_points(u_2, v_2, deg)
    ru_3, rv_3 = rotate_points(u_3, v_3, deg)
    ru_4, rv_4 = rotate_points(u_4, v_4, deg)
    ru_5, rv_5 = rotate_points(u_5, v_5, deg)
    ru_6, rv_6 = rotate_points(u_6, v_6, deg)
    ru_7, rv_7 = rotate_points(u_7, v_7, deg)
    ru_8, rv_8 = rotate_points(u_8, v_8, deg)
    ru_9, rv_9 = rotate_points(u_9, v_9, deg)
    ru_10, rv_10 = rotate_points(u_10, v_10, deg)

    # out.plot(ru_1, rv_1, 'r', linewidth=3.0) 
    # out.plot(ru_2, rv_2, 'b', linewidth=3.0)  

except Exception as e:
    pass

# just add new out.plot statements as and when required
graph = plt.figure()
out = graph.add_subplot(1,1,1)
out.set_aspect('equal')
try:
    out.plot(ru_1, rv_1, 'k', linewidth=5.0)
    out.plot(ru_2, rv_2, 'k', linewidth=5.0)
    out.plot(ru_3, rv_3, 'k', linewidth=5.0)
    out.plot(ru_4, rv_4, 'k', linewidth=5.0)
    out.plot(ru_5, rv_5, 'k', linewidth=5.0)
    out.plot(ru_6, rv_6, 'k', linewidth=5.0)
    out.plot(ru_7, rv_7, 'k', linewidth=5.0)
    out.plot(ru_8, rv_8, 'k', linewidth=5.0)
    out.plot(ru_9, rv_9, 'k', linewidth=5.0)
    out.plot(ru_10, rv_10, 'k', linewidth=5.0)
    
except:
    pass
out.axis('off')
plt.savefig(name)
# plt.show()