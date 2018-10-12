import csv
training = []
with open('iris.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        training = training+[row]
#conversion of data-sets to a list
training = training[:-1] # truncated the last one
#print training
print "Data details"
print "Total samples", len(training)
#Conversion of "Iris-Sesots" to 1 and "Iris-virginica" to -1"
for sample in training:
    if sample[4] =="Iris-setosa":
        sample[4] = 1
    else:
        sample[4] = -1
        
#Truncate X and d values
X = []
for sample in training:
    X = X+[sample[:4]]
print X, len(X)
    
d = []
for sample in training:
    d = d+[sample[-1]]
print d, len(d)