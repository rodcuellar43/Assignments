#!/usr/bin/env python
# coding: utf-8

# # Homework 4 - Due Friday Sept 11, 5pm

# *The semi-empirical mass formula*
# 
# In nuclear physics, the semi-empirical mass formula is a formula for calculating the
# approximate nuclear binding energy $B$ of an atomic nucleus with atomic number $Z$
# and mass number $A$. The formula looks like this:
#     
# $$ B = a_1 A - a_2 A^{2/3} - a_3 \frac{Z^2}{A^{1/3}} - a_4 \frac{(A - 2Z)^2}{A} - \frac{a_5}{A^{1/2}} $$
# 
# where, in units of millions of electron volts (MeV), the constants are $a_1 =
# 15.67$, $a_2 = 17.23$, $a_3 = 0.75$, $a_4 = 93.2$, and
# 
# $$ a_5  \; =  \;\; \left\{ \begin{array} {r@{\quad\tt if \quad}l} 0 & A \;{\tt is
#       \; odd}, \\
#     12.0 & A \;{\tt and}\; Z \;{\tt are \;both \;even}, \\ -12.0 & A \;{\tt is
#      \;  even \; and}\;  Z \;{\tt is
#   \;  odd.} \end{array} \right. $$
# 
# Write a function that takes as its input the values of $A$ and $Z$, and
# prints out: 
# * (a) the binding energy $B$ for the corresponding atom and 
# * (b) the binding energy per nucleon, which is $B/A$. 
# 
# Use your program to find
# the binding energy of an atom with $A = 58$ and $Z = 28$. (Hint: The
# correct answer is around 490 MeV.) 
# 
# Also run,  $A = 59$ and $Z = 28$ and $A = 58$ and $Z = 27$.
# 

# In[6]:


import math

def getNuclerBindingEnergy(A, Z):
    a1 = 15.67
    a2 = 17.23
    a3 = 0.75
    a4 = 93.2
    a5 = 0
  
    if A % 2 == 1:
        a5 = 0
    else:
        if Z % 2 == 0:
            a5 = 12.0
        else:
            a5 = -12.0
  
    B = a1*A - a2*math.pow(A, 2/3) - a3*(Z*Z/math.pow(A, 1/3)) - a4*(math.pow(A-2*Z, 2)/A) + a5/math.pow(A, 1/2)
  
    return B

def getNuclerBindingEnergyPerNucleon(A, Z):
    return getNuclerBindingEnergy(A, Z) / A

def getStableNucleus(Z):
    max = 0.0
    maxA = 0
  
    for A in range(Z, 3*Z + 1):
        bindingEnergy = getNuclerBindingEnergyPerNucleon(A, Z)
        if max < bindingEnergy:
            max = bindingEnergy
            maxA = A
  
    return max, maxA

def findOverallStableNucleus():
    maxZ = 0
    max = 0.0
  
    for Z in range(1, 101):
        currentMax, maxA = getStableNucleus(Z)
        print("Z = %d: The maximum binding enery per nucleon = %f Mev for A = %d" % (Z, currentMax, maxA))

        if max < currentMax:
            max = currentMax
            maxZ = Z
  
    print("The overall maximum binding energy per nucleon occur at Z = %d" % maxZ)

print("The binding enery for the corresponding atom is: %f MeV" % getNuclerBindingEnergy(58, 28))

print("The binding enery per nucleon for the corresponding atom is: %f MeV" % getNuclerBindingEnergyPerNucleon(58, 28))

Z = int(input("Enter the value of Z : "))
max, maxA = getStableNucleus(Z)
print("Z = %d: The maximum binding enery per nucleon = %f Mev for A = %d" % (Z, max, maxA))

print("Finding the maximum Z now..........")
findOverallStableNucleus()


# In[ ]:




