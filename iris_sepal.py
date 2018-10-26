#This code plots the graph for IRIS dataset sepal length vs sepal width
#import pandas
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches


import csv
training = []
with open('iris.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        training = training+[row]
	
#conversion of data-sets to a list
training = training[:-1] # truncated the last one
print training
print "Data details"
print "Total samples", len(training)

flower_type = [x[4] for x in training]

for i in range(len(training)):
    x,y = [training[i][0],training[i][1]]
    scale=100
    flower = flower_type[i].decode("utf-8")
    color = ""
    if flower == "Iris-setosa":
		color = "red"

    elif flower == "Iris-versicolor":
		color = "green"
    elif flower == "Iris-virginica":
		color = "blue"

    plt.scatter(x, y, s=scale, c=color, alpha=1, edgecolor="none")

# Legend
red_patch = mpatches.Patch(color='red', label='iris setosa')
green_patch = mpatches.Patch(color='green', label='iris versicolor')
blue_patch = mpatches.Patch(color='blue', label='iris virginica')
plt.legend(handles=[red_patch, green_patch, blue_patch])

plt.title("The Iris Data Set", fontsize=18)
plt.xlabel(r'Sepal length', fontsize=15)
plt.ylabel(r'Sepal width', fontsize=15)
plt.show()
