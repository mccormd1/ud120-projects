#!/usr/bin/python

""" lecture and example code for decision tree unit """

import sys
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
##from classifyDT import classify

def classify(features_train, labels_train):
    
    ### your code goes here--should return a trained decision tree classifer
 from sklearn.tree import DecisionTreeClassifier
 clf=DecisionTreeClassifier(min_samples_split=2)
 clf.fit(features_train,labels_train)
    
    
 return clf


features_train, labels_train, features_test, labels_test = makeTerrainData()



### the classify() function in classifyDT is where the magic
### happens--fill in this function in the file 'classifyDT.py'!
clf = classify(features_train, labels_train)

#predictions=clf.predict(features_test)

#acc=100*(1-sum(abs(predictions-labels_test))/len(predictions))

acc=clf.score(features_test,labels_test)
print (acc)

prettyPicture(clf, features_test, labels_test)
#output_image("test.png", "png", open("test.png", "rb").read())
#plt.show()