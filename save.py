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
name = 'घ'
x_p1 = 3 + 6*t
y_p1 = 10 + 0*t

x_p2 = 8 + 0*t
y_p2 = 2 + 8*t

x_p3 = 6 + 2.25*np.cos(5*pe/6 + (4*pe/6)*t)
y_p3 = 8.8 + 2.25*np.sin(5*pe/6 + (4*pe/6)*t)

x_p4 = 6 + 1.75*np.cos(pe/2 + (7*pe/6)*t)
y_p4 = 4.75 + 1.75*np.sin(pe/2 + (7*pe/6)*t)

x_p5 = 6 + 1.75*np.cos(pe/2 + (7*pe/6)) + 1*t
y_p5 = 4.75 + 1.75*np.sin(pe/2 + (7*pe/6)) + 0.6*t


#ङ
# x_p1 = 7.5 + 3*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 8 + 2*t

# x_p3 = 9 + 3.25*np.cos(pe/2 + (pe)*t)
# y_p3 = 5.75 + 2.25*np.sin(pe/2 + (pe)*t)

# x_p4 = 9 + 2.50*np.cos((3*pe/2 - 1.2) + (pe + 1.2)*t)
# y_p4 = 1.5 + 2*np.sin((3*pe/2 - 1.2) + (pe + 1.2)*t)

# x_p5 = 10.5 + 0.5*np.cos((2*pe)*t)
# y_p5 = 5.75 + 0.5*np.sin((2*pe)*t)


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


# छ
# x_p1 = 7.5 + 3*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 8.5 + 1.5*t

# x_p3 = 9 + 2*np.cos(pe/2 + (pe)*t)
# y_p3 = 7 + 1.5*np.sin(pe/2 + (pe)*t)

# x_p4 = 9 + 1.75*np.cos(pe/2 + (5*pe/4)*t)
# y_p4 = 3.75 + 1.75*np.sin(pe/2 + (5*pe/4)*t)

# x_p5 = 9.9 + 0.5*np.cos(2*pe*t)
# y_p5 = 2.9 + 0.5*np.sin(2*pe*t)


#ज
# x_p1 = 2 + 8.5*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 6 + 3*t
# y_p3 = 6.5 + 0*t

# x_p4 = 4.8 + 1.75*np.cos(5*pe/4 + (pe)*t)
# y_p4 = 5.25 + 1.75*np.sin(5*pe/4 + (pe)*t)

# x_p5 = 4.8 + 1.75*np.cos(5*pe/4) - 1.5*t
# y_p5 = 5.25 + 1.75*np.sin(5*pe/4) + 1.5*t


# झ
# x_p1 = 7.5 + 9*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 8 + 2*t

# x_p3 = 9 + 3.25*np.cos(pe/2 + (pe)*t)
# y_p3 = 5.75 + 2.25*np.sin(pe/2 + (pe)*t)

# x_p4 = 9 + 2.75*np.cos((3*pe/2 - 0.3) + (pe + 0.3)*t)
# y_p4 = 1.25 + 2.25*np.sin((3*pe/2 - 0.3) + (pe + 0.3)*t)

# x_p5 = 8 + 0.5*np.cos(pe/4 + (5*pe/4)*t)
# y_p5 = -0.36 + 0.5*np.sin(pe/4 + (5*pe/4)*t)

# x_p6 = 8 + 0.5*np.cos(pe/4) + 2*t
# y_p6 = -0.36 + 0.5*np.sin(pe/4) - 2*t

# x_p7 = 14.5 + 0*t
# y_p7 = -2 + 12*t

# x_p8 = 14.5 - 3.5*t
# y_p8 = 2.9 + 0*t


#ञ
# x_p1 = 2 + 7.5*t
# y_p1 = 10 + 0*t

# x_p2 = 8 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 6 + 2*t
# y_p3 = 6.5 + 0*t

# x_p4 = 4.2 + 1.75*np.cos(5*pe/4 + (3*pe/2)*t)
# y_p4 = 6.5 + 1.75*np.sin(5*pe/4 + (3*pe/2)*t)

# x_p5 = 4.2 + 1.75*np.cos(5*pe/4) - 1.5*t
# y_p5 = 6.5 + 1.75*np.sin(5*pe/4) + 1.5*t


#ट
# x_p1 = 5 + 5.5*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 8.5 + 1.5*t

# x_p3 = 8.15 + 3*np.cos(pe/3 + 0.25 + (4*pe/3)*t)
# y_p3 = 5.85 + 2.75*np.sin(pe/3 + 0.25 + (4*pe/3)*t)


#ठ
# x_p1 = 5 + 5.5*t
# y_p1 = 10 + 0*t

# x_p2 = 7.5 + 0*t
# y_p2 = 9 + 1*t

# x_p3 = 7.5 + 3*np.cos(2*pe*t)
# y_p3 = 6.2 + 2.75*np.sin(2*pe*t)


#ड
# x_p1 = 7.5 + 3*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 8 + 2*t

# x_p3 = 9 + 3.25*np.cos(pe/2 + (pe)*t)
# y_p3 = 5.75 + 2.25*np.sin(pe/2 + (pe)*t)

# x_p4 = 9 + 2.50*np.cos((3*pe/2 - 1.2) + (pe + 1.2)*t)
# y_p4 = 1.5 + 2*np.sin((3*pe/2 - 1.2) + (pe + 1.2)*t)


#ढ
# x_p1 = 5 + 5.5*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 8.5 + 1.5*t

# x_p3 = 8.15 + 3*np.cos(pe/3 + 0.25 + (4*pe/3)*t)
# y_p3 = 5.85 + 2.75*np.sin(pe/3 + 0.25 + (4*pe/3)*t)

# x_p4 = 10 + 0.5*np.cos(2*pe*t)
# y_p4 = 4.325 + 0.5*np.sin(2*pe*t)


# ण
# x_p1 = 2 + 8*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 6 + 0*t
# y_p3 = 5 + 5*t

# x_p4 = 3 + 0*t
# y_p4 = 5 + 5*t

# x_p5 = 4.5 + 1.5*np.cos(pe + pe*t)
# y_p5 = 5 + 1*np.sin(pe + pe*t)


#त
# x_p1 = 2 + 7.5*t
# y_p1 = 10 + 0*t

# x_p2 = 8 + 0*t
# y_p2 = 1 + 9*t

# x_p3 = 4.5 + 3.5*t
# y_p3 = 7 + 0*t

# x_p4 = 4.5 + 1.75*np.cos(pe/2 + (2*pe/3)*t)
# y_p4 = 5.25 + 1.75*np.sin(pe/2 + (2*pe/3)*t)

# x_p5 = 4.5 + 1.75*np.cos(pe/2 + (2*pe/3)) + 1.5*t
# y_p5 = 5.25 + 1.75*np.sin(pe/2 + (2*pe/3)) - 3*t


#थ
# x_p1 = 2 + 8*t
# y_p1 = 10 + 0*t

# x_p2 = 8 + 0*t
# y_p2 = 1 + 9*t

# x_p3 = 4 + 0.5*np.cos(2*pe*t)
# y_p3 = 9.5 + 0.5*np.sin(2*pe*t)

# x_p4 = 2.3 + 3*np.cos(7*pe/4 - 0.4 + (pe/3 + 0.9)*t)
# y_p4 = 7.75 + 3*np.sin(7*pe/4 - 0.4 + (pe/3 + 0.9)*t)

# x_p5 = 6 + 3*np.cos(5*pe/4 - 0.3 + (pe/3 + 0.72)*t)
# y_p5 = 6.3 + 3*np.sin(5*pe/4 - 0.3 + (pe/3 + 0.72)*t)


#द
# x_p1 = 5 + 5.5*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 8.5 + 1.5*t

# x_p3 = 8.15 + 3*np.cos(pe/3 + 0.25 + (4*pe/3)*t)
# y_p3 = 5.85 + 2.75*np.sin(pe/3 + 0.25 + (4*pe/3)*t)

# x_p4 = 10 + 0.5*np.cos(3*pe/2 + 0.6 + (3*pe/2)*t)
# y_p4 = 4.325 + 0.5*np.sin(3*pe/2 + 0.6 + (3*pe/2)*t)

# x_p5 = 10.025 + 0.5*np.cos(3*pe + 0.2) + 1.5*t
# y_p5 = 4.25 + 0.5*np.sin(3*pe + 0.2) - 2.5*t

#ध
# x_p1 = 3 + 6*t
# y_p1 = 10 + 0*t

# x_p2 = 8 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 6 + 2.25*np.cos(5*pe/6 + (4*pe/6)*t)
# y_p3 = 8.8 + 2.25*np.sin(5*pe/6 + (4*pe/6)*t)

# x_p4 = 6 + 1.75*np.cos(pe/2 + (7*pe/6)*t)
# y_p4 = 4.75 + 1.75*np.sin(pe/2 + (7*pe/6)*t)

# x_p5 = 6 + 1.75*np.cos(pe/2 + (7*pe/6)) + 1*t
# y_p5 = 4.75 + 1.75*np.sin(pe/2 + (7*pe/6)) + 0.6*t

# x_p6 = 4.5 + 0.5*np.cos(2*pe*t)
# y_p6 = 9.5 + 0.5*np.sin(2*pe*t)


# न
# x_p1 = 4 + 7*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 5 + 4*t
# y_p3 = 7 + 0*t

# x_p4 = 5 + 0.5*np.cos(2*pe*t)
# y_p4 = 6.5 + 0.5*np.sin(2*pe*t)


#प
# x_p1 = 2 + 7*t
# y_p1 = 10 + 0*t

# x_p2 = 7.5 + 0*t
# y_p2 = 0 + 10*t

# x_p3 = 3.5 + 0*t
# y_p3 = 5 + 5*t

# x_p4 = 5.5 + 2*np.cos(pe + pe*t)
# y_p4 = 5 + 1.5*np.sin(pe + pe*t)


#फ
# x_p1 = 2 + 10*t
# y_p1 = 10 + 0*t

# x_p2 = 7.5 + 0*t
# y_p2 = 0 + 10*t

# x_p3 = 3.5 + 0*t
# y_p3 = 5 + 5*t

# x_p4 = 5.5 + 2*np.cos(pe + pe*t)
# y_p4 = 5 + 1.5*np.sin(pe + pe*t)

# x_p5 = 9.2 + 2.25*np.cos(7*pe/4 + (pe)*t)
# y_p5 = 3.5 + 2.25*np.sin(7*pe/4 + (pe)*t)


# ब
# x_p1 = 5 + 6*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 7.25 + 1.75*np.cos(0 + (2*pe)*t)
# y_p3 = 6 + 1.75*np.sin(0 + (2*pe)*t)

# x_p4 = 6 + 2.5*t
# y_p4 = 7.25 - 2.5*t


#भ
# x_p1 = 4 + 7*t
# y_p1 = 10 + 0*t

# x_p2 = 9.5 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 5.5 + 0*t
# y_p3 = 3 + 6.5*t

# x_p4 = 5 + 0.5*np.cos(2*pe*t)
# y_p4 = 9.5 + 0.5*np.sin(2*pe*t)

# x_p5 = 9.5 - 5*t
# y_p5 = 4 - 0*t

# x_p6 = 5.5 + 1*np.cos(pe + (pe/2)*t)
# y_p6 = 4 + 1*np.sin(pe + (pe/2)*t)


# म
# x_p1 = 4 + 7*t
# y_p1 = 10 + 0*t

# x_p2 = 9.5 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 5.5 + 0*t
# y_p3 = 3 + 7*t

# x_p4 = 9.5 - 5*t
# y_p4 = 4 - 0*t

# x_p5 = 5.5 + 1*np.cos(pe + (pe/2)*t)
# y_p5 = 4 + 1*np.sin(pe + (pe/2)*t)


#य
# x_p1 = 2 + 8*t
# y_p1 = 10 + 0*t

# x_p2 = 8 + 0*t
# y_p2 = 1 + 9*t

# x_p3 = 2.3 + 3*np.cos(7*pe/4 - 0.4 + (pe/3 + 0.95)*t)
# y_p3 = 7.75 + 3*np.sin(7*pe/4 - 0.4 + (pe/3 + 0.95)*t)

# x_p4 = 6 + 3*np.cos(5*pe/4 - 0.3 + (pe/3 + 0.72)*t)
# y_p4 = 6.3 + 3*np.sin(5*pe/4 - 0.3 + (pe/3 + 0.72)*t)

# र
# x_p1 = 7.5 + 5*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 2.25*np.cos(3*pe/2 + (pe)*t)
# y_p2 = 7.75 + 2.25*np.sin(3*pe/2 + (pe)*t)

# x_p3 = 9 + 0.5*np.cos(pe/4 + (5*pe/4)*t)
# y_p3 = 6 + 0.5*np.sin(pe/4 + (5*pe/4)*t)

# x_p4 = 9 + 0.5*np.cos(pe/4) + 3*t
# y_p4 = 6 + 0.5*np.sin(pe/4)- 3*t

# x_p5 = 12.9 + 1*np.cos(3*pe/2 - pe/6 + (pe/3)*t)
# y_p5 = 4.20 + 1*np.sin(3*pe/2 - pe/6  + (pe/3)*t)


#ल
# x_p1 = 3 + 8*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 9 - 3*t
# y_p3 = 7.5 - 2*t

# x_p4 = 5.75 + 2.25*np.cos(pe/4 + (pe)*t)
# y_p4 = 4.95 + 2.25*np.sin(pe/4 + (pe)*t)

# x_p5 = 5.75 + 2.25*np.cos(5*pe/4) + 1*t
# y_p5 = 4.95 + 2.25*np.cos(5*pe/4) - 1*t


# व
# x_p1 = 5 + 6*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 7.25 + 1.75*np.cos(0 + (2*pe)*t)
# y_p3 = 6 + 1.75*np.sin(0 + (2*pe)*t)


# श
# x_p1 = 2 + 8*t
# y_p1 = 10 + 0*t

# x_p2 = 3 + 2.25*np.cos(3*pe/2 + (pe)*t)
# y_p2 = 7.75 + 2.25*np.sin(3*pe/2 + (pe)*t)

# x_p3 = 3 + 0.5*np.cos(pe/4 + (5*pe/4)*t)
# y_p3 = 6 + 0.5*np.sin(pe/4 + (5*pe/4)*t)

# x_p4 = 3 + 0.5*np.cos(pe/4) + 3*t
# y_p4 = 6 + 0.5*np.sin(pe/4)- 3*t

# x_p5 = 6.9 + 1*np.cos(3*pe/2 - pe/6 + (pe/3)*t)
# y_p5 = 4.20 + 1*np.sin(3*pe/2 - pe/6  + (pe/3)*t)

# x_p6 = 3.3 + 0.5*np.cos(2*pe*t)
# y_p6 = 9.5 + 0.5*np.sin(2*pe*t)

# x_p7 = 9 + 0*t
# y_p7 = 3 + 7*t


# ष
# x_p1 = 2 + 7*t
# y_p1 = 10 + 0*t

# x_p2 = 7.5 + 0*t
# y_p2 = 0 + 10*t

# x_p3 = 3.5 + 0*t
# y_p3 = 5 + 5*t

# x_p4 = 5.5 + 2*np.cos(pe + pe*t)
# y_p4 = 5 + 1.5*np.sin(pe + pe*t)

# x_p5 = 3.5 + 4*t
# y_p5 = 10 - 5*t


# स
# x_p1 = 2 + 8*t
# y_p1 = 10 + 0*t

# x_p2 = 3 + 2.25*np.cos(3*pe/2 + (pe)*t)
# y_p2 = 7.75 + 2.25*np.sin(3*pe/2 + (pe)*t)

# x_p3 = 3 + 0.5*np.cos(pe/4 + (5*pe/4)*t)
# y_p3 = 6 + 0.5*np.sin(pe/4 + (5*pe/4)*t)

# x_p4 = 3 + 0.5*np.cos(pe/4) + 3*t
# y_p4 = 6 + 0.5*np.sin(pe/4)- 3*t

# x_p5 = 6.9 + 1*np.cos(3*pe/2 - pe/6 + (pe/3)*t)
# y_p5 = 4.20 + 1*np.sin(3*pe/2 - pe/6  + (pe/3)*t)

# x_p6 = 5 + 4*t
# y_p6 = 6.5 + 0*t

# x_p7 = 9 + 0*t
# y_p7 = 3 + 7*t

# ह
# x_p1 = 5 + 8*t
# y_p1 = 10 + 0*t

# x_p2 = 10.65 + 0*t
# y_p2 = 7.75 + 2.25*t

# x_p3 = 9 + 3.25*np.cos(pe/2 - 0.5+ (pe)*t)
# y_p3 = 5.75 + 2.25*np.sin(pe/2 - 0.5 + (pe)*t)

# x_p4 = 9 + 3.25*np.cos(7*pe/4 - 0.4 + (3*pe/2 + 0.4)*t)
# y_p4 = 1.75 + 2.25*np.sin(7*pe/4 - 0.4 + (3*pe/2 + 0.4)*t)

# x_p5 = 9 + 3.25*np.cos(5*pe/4) + 3*t
# y_p5 = 1.75 + 2.25*np.sin(5*pe/4) - 2*t


# क्ष
# x_p1 = 2 + 8*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 5 + 4*t
# y_p3 = 7 + 0*t

# x_p4 = 5 + 0.75*np.cos(2*pe*t)
# y_p4 = 7.75 + 0.75*np.sin(2*pe*t)

# x_p5 = 5 + 1.75*np.cos(pe/2 + (pe + pe/6)*t)
# y_p5 = 5.25 + 1.75*np.sin(pe/2 + (pe + pe/6)*t)

# x_p6 = 5.7 + 0.5*np.cos(3*pe/2 + pe/6 + (3*pe/2)*t)
# y_p6 = 4.21 + 0.5*np.sin(3*pe/2 + pe/6 + (3*pe/2)*t)

# x_p7 = 5.7 + 0.5*np.cos(3*pe + pe/6) + 1*t
# y_p7 = 4.21 + 0.5*np.sin(3*pe + pe/6) - 2*t


# त्र
# x_p1 = 2.5 + 6.5*t
# y_p1 = 10 + 0*t

# x_p2 = 7.5 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 7.5 - 2.5*t
# y_p3 = 6 + 2*t

# x_p4 = 7.5 - 4*t
# y_p4 = 6 - 3*t

# x_p5 = 5 - 2*t
# y_p5 = 8 - 1*t

# ज्ञ
# x_p1 = 1 + 9.5*t
# y_p1 = 10 + 0*t

# x_p2 = 9 + 0*t
# y_p2 = 2 + 8*t

# x_p3 = 6 + 3*t
# y_p3 = 6.5 + 0*t

# x_p4 = 4.8 + 1.75*np.cos(5*pe/4 + (pe)*t)
# y_p4 = 5.25 + 1.75*np.sin(5*pe/4 + (pe)*t)

# x_p5 = 4.8 + 1.75*np.cos(5*pe/4) - 1.5*t
# y_p5 = 5.25 + 1.75*np.sin(5*pe/4) + 1.5*t

# x_p6 = 2.31 + 0.5*np.cos(pe/4 - pe/6 + (pe + pe/6)*t)
# y_p6 = 5.98 + 0.5*np.sin(pe/4 - pe/6 + (pe + pe/6)*t)

# x_p7 = 2.31 + 0.5*np.cos(pe/4 - pe/6) + 0.5*t
# y_p7 = 5.98 + 0.5*np.sin(pe/4 - pe/6) - 3*t

# 'श्र'
# x_p1 = 2 + 8*t
# y_p1 = 10 + 0*t

# x_p2 = 8.5 + 0*t
# y_p2 = 0 + 10*t

# x_p3 = 8.5 - 3.3*t
# y_p3 = 5 + 2.2*t

# x_p4 = 6.10 - 3*t
# y_p4 = 7.2 - 2*t

# x_p5 = 8.5 - 4.8*t
# y_p5 = 5 - 4*t

# x_p6 = 5.65 + 0.75*np.cos(7*pe/4 + (2*pe - pe/2)*t)
# y_p6 = 7.8 + 0.75*np.sin(7*pe/4 + (2*pe - pe/2)*t)



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
    deg = -45
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
plt.savefig(name, transparent=True)
# plt.show()