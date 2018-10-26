#Implements the perceptron rule for IRIS dataset

import numpy as np
import iris 

#print iris.X
#print iris.d
#Training

X = iris.X
X = np.array(X)
print "Input values"
print X

d = iris.d
d = np.array(d)
print "Teacher values"
print d
print "length", len(d)

print "initial weights"
w = np.zeros(4)
print w
c = 0.1

y=X.astype(np.float)
print y.dtype

for n in range(1,5):
    for i, x in enumerate(y):
        net = np.dot(y[i],w) 
        if net > 0:
            out = 1
        else:
            out = -1
        r = c*(d[i] - out)
        delta_w = r*x
        w = delta_w+w
    print n, i, w
final_out = []
#Testing
print "Testing"
for i,x in enumerate(y):
    net = np.dot(y[i],w)
    if net>0:
        out = 1
    else:
        out = -1
    final_out = final_out+[out]
print "final output", final_out
print "d", d





