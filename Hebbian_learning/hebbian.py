#This is a toy problem explaining Hebbian Learning
#This is an unsupervised Learning
import numpy as np
X = np.array([[1,-2,1.5,0],[0,1.5,-0.5,-1],[-1,1,0.5,-1],])
print "Inputs", X
w = ([1,-1,0,0.5])
print "initial weights", w
iterations = 7
alpha = 1
print "Training"
print "------------"
for n in range(1,iterations):
    for i, x in enumerate(X):
        net = np.dot(X[i],w)
        if net >0:
            out = 1
        else:
            out = -1
        delta_w = (alpha)*(out)*x
        w = w + delta_w
        print "------------"
        print "input x",x
        print n, i, w
        print "output",out
        print "------------"
print "Final sets of weights", w
