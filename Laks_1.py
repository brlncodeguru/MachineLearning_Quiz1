#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 10:34:15 2017

@author: lakshminarayanabr
"""

import numpy as np





#Read the data from the path and separate each coloumn into one variable and have an extra variable with all three combined coloumn wise
data=np.recfromcsv("/Users/lakshminarayanabr/Downloads/dataset_1.csv")
x=data["x"]
y=data["y"]
z=data['z']
final_data = np.array([x,y,z])



#(1)Calculating variance of each variable x,y and z
var_x=x.var()
var_y=y.var()
var_z=z.var()

print "Variance of x "
print var_x

print "Variance of y "
print var_y


print "Variance of z "
print var_z







#Calculate mean of each variable x,y and z 
mean_x = np.mean(x)
mean_y = np.mean(y)
mean_z = np.mean(z)

mean_vector = np.array([[mean_x],[mean_y],[mean_z]])
print('Mean Vector:', mean_vector)

#(2)Covariance


#Calculating Covariance between X & Y
mean_xy=np.mean(x*y)
cov_XY=mean_xy-(mean_x*mean_y)
cov_XY
print('Covariance Matrix  between X & Y:',cov_XY)

#Calculating covariance between Y & Z
mean_yz=np.mean(y*z)
cov_YZ=mean_yz-(mean_y*mean_z)
cov_YZ
print('Covariance Matrix  between Y & Z:',cov_YZ)


#(3)PCA 

#Calculate covariance individually for each coloumn
cov_mat = np.cov([x,y,z])
print('Covariance Matrix:', cov_mat)



#Calculate the Eigen values and Eigen vectors using the covariance matrix
eig_val_cov, eig_vec_cov = np.linalg.eig(cov_mat)

#making key value pairs of the eigen vectors and eigen values
eig_pairs = [(np.abs(eig_val_cov[i]), eig_vec_cov[:,i]) for i in range(len(eig_val_cov))]
eig_pairs.sort(key=lambda x: x[0], reverse=True)

for i in eig_pairs:
    print('Eigen values in descedning order:',i[0])
    
matrix_w = np.hstack((eig_pairs[0][1].reshape(3,1), eig_pairs[1][1].reshape(3,1)))
print('Matrix W:\n', matrix_w)


transformed = matrix_w.T.dot(final_data)
print('Transformed matrix after dimensional reduction:',transformed)

