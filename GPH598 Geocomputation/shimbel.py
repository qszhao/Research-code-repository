# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:44:19 2013

@author: qszhao
"""
import numpy as np
#fp = open('e08_small.gal','r')
#fp = open('e06.gal','r')
fp = open('columbus.gal','r')
line = fp.readline()
serial = line.split()
num = int(serial[0])
lines = fp.readlines()  
census = [map(int,l.strip().split()) for l in lines]
array = np.zeros((num,num))
i = 0
# Get the C1
while i < (num*2):
    jj = census[i][0]-1    
    ii = census[i][1]
    j = 0    
    while j<ii:
        aa = census[i+1][j]-1        
        array[jj][aa]=1
        j += 1
    i += 2    
    
shimbel = np.copy(array)
matrix = np.copy(array)
t = 1


while t <> 0:   
   i = 0
   j = 0 
   k = 0
# If shimbel matrix has 0, calculate C2   
   while i < num and k <> 1:
        while j < num and k <> 1:
            if shimbel[i][j]==0:
                t += 1
                #flag = t
                matrix = np.dot(matrix,array)
                k = 1
            j += 1
        i += 1
        j = 0
# Replace shimbel matrix by C matrix
   for i in range(num):
       for j in range(num):
           if matrix[i][j]!=0 and shimbel[i][j]==0:
               shimbel[i][j] = t
# If shimbel matrix has 0, continue the loop. If not, stop.                
   i = 0
   j = 0
   kk = 0      
   while i < num and kk <> 1:
        while j < num and kk <> 1:
           if shimbel[i][j]==0:
               kk = 1
           j += 1
        i += 1     
        j = 0
   if kk == 0:
       t = 0
'''
for i in range(num):
       for j in range(num):
           if shimbel[i][j] == 0:
               shimbel[i][j] = flag+1
'''         
# Let the diagonal = 0
for i in range(num):
    shimbel[i][i]=0
    
diameter = 0
summary = 0
# Diameter and average
for i in range(num):
       for j in range(num):
           if shimbel[i][j] > diameter:
               diameter = shimbel[i][j]
           summary += shimbel[i][j]
           average = summary/(num*(num-1))
           
print 'Shimbel matrix is:','\n',shimbel
print 'diameter = ',diameter,'\n','average = ',average
# For each node attributes          
dic = {}
# Shimbel index
for i in range(num):
    summ = 0    
    for j in range(num):
        order = []        
        summ += shimbel[i][j]
        order.append(summ)
        dic[i+1] = order
# Order of the node
i = 0        
while i < (num*2):
    dic[i/2+1].append(census[i][1])     
    i += 2
# Average nearest neighbors degree    
i = 0
while i < (num*2):    
    summ = 0        
    l = census[i][1]        
    for j in range(l):
        summ += dic[census[i+1][j]][1]        
    average = summ*1./census[i][1]     
    dic[i/2+1].append(average)
    i += 2        

print "Each node's attributes are", '\n' , dic
    
    

    

    
