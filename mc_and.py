#McCulloh Pitt model for AND model
import numpy as np

def McAnd(x,w,t):
    net = np.dot(x,w)
    if net>t:
        output = 1
    else:
        output = 0
    return output

## MP-OR
def McOR(x,w,t):
    net = np.dot(x,w)
    #Using Bipolar Activation
    if net>t:
        output = 1
    else:
        output = -1
    return output

## MP-NOT
def McNot(x,w,t):
    #Using Sigmoidal Activation
    net = np.dot(x,w);
    out = 1/(1+np.exp(-0.1*net));
    if out>0.5:
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

### Testing MP-OR
o0 = np.array([0,0,1])
o1 = np.array([0,1,1])
o2 = np.array([1,0,1])
o3 = np.array([1,1,1])
ow = np.array([2,2,-1])

t = 0
ans1 = McOR(o0,ow,t)
print (x0, "value", ans1)
ans2 = McOR(o1,ow,t)
print (x1, "value", ans2)
ans3 = McOR(o2,ow,t)
print (x2, "value", ans3)
ans4 = McOR(o3,ow,t)
print (x3, "value", ans4)

### Testing MP-NOT
n0 = np.array([0,1])
n1 = np.array([1,1])
w = np.array([-1,1])

t = 0
ans1 = McNot(n0,w,t)
print (x0, "value", ans1)
ans2 = McNot(n1,w,t)
print (x1, "value", ans2)
