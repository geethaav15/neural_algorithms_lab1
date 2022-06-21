#McCulloh Pitt model for AND model
import numpy as np

def McAnd(x,w,t):
    net = np.dot(x,w)
    if net>t:
        output = 1
    else:
        output = 0
    return output

x0 = np.array([0,0,1])
x1 = np.array([0,1,1])
x2 = np.array([1,0,1])
x3 = np.array([1,1,1])
w = np.array([1,1,-1])

t = 0
ans1 = McAnd(x0,w,t)
print (x0, "value", ans1)
ans2 = McAnd(x1,w,t)
print (x1, "value", ans2)
ans3 = McAnd(x2,w,t)
print (x2, "value", ans3)
ans4 = McAnd(x3,w,t)
print (x3, "value", ans4)
