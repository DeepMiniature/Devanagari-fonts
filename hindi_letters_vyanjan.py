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


#घ
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

# श्र
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