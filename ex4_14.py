#zurada exercise 4.14
import numpy as np

def bipolar(x):
    return (2/(1+np.exp(-x))-1)

z = np.array([1,3,-1])
v = np.array([[1,-2,3],[2,0,-1]])
w = np.array([[1,0,-2],[1,-2,3]])
d = np.array([0.95,0.05])
e = np.zeros(2,)
eta = 0.8

print ("input z", z)
print("weights ", v)
print("weights", w)
print("d values", d)
#find y
net1 = np.dot(v,z)
print("net values of v and z:", net1)
y = []
for i in net1:
    out = bipolar(i)
    y = y+[out]
aug = [-1.0]
y = y+aug
y = np.array(y)
print("y values are: ")
print(y)
#print("shape of w", w.shape)
#print ("shape of y", y.shape)
#find o
net2 = np.dot(w,y)
print("net values of w and y:", net2)
ot = []
for j in net2:
    out = bipolar(j)
    ot = ot+[out]
ot = np.array(ot)
print("output values are ")
print(ot)
#calculation of errors
error = (np.square(d-ot))+e
print("error - ", error)
#calculation of deltaok
onem = np.ones(2,)
print(onem)
deltaok = 0.5*(d-ot)*(1-(ot*ot))
print("deltaok value", deltaok)
#calculation of deltayj
deltaokw = deltaok.dot(w)
print(deltaokw)
deltayj = 0.5*(1-(y*y))*deltaokw
print("deltayj value ", deltayj)
#change in weights, w and v
yt = y.reshape(1,3)
deltaok = deltaok.reshape(2,1)
print("shape of y ", y.shape)
print ("shape of yt", yt.shape)
print("shape of deltaok", deltaok.shape)
deltaoky = np.multiply(deltaok,yt)
print("value of deltaok with y", deltaoky)
w = w+(eta*deltaoky)
print("new weights w ", w)
