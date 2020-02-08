#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 13:03:48 2020

@author: bruno
"""

import numpy as np
import matplotlib.pyplot as plt


# foil thickness normalized with respect to skin depth
A = np.geomspace(0.1, 10.0, 100)

# number of layers from 0.5 to 10
layers = np.array([0.5])
layers = np.append(layers, np.arange(1,11,1))

# Dowell's formula

def dowell(A, N):
    f = A * ((np.sinh(2*A) + np.sin(2*A)) / (np.cosh(2*A) - np.cos(2*A)) +
             2 * (N**2 - 1) / 3 * 
             (np.sinh(A) - np.sin(A)) / (np.cosh(A) + np.cos(A)))
    return f

# Calculation for all layers over range of A
    
Fr = np.zeros((len(layers), len(A)))

for i in range(len(layers)) :
    x = dowell(A, layers[i])
    Fr[i] = x

# plot of the curves
plt.rc('mathtext', fontset='stix')
plt.figure(1, figsize=(12,8))

for i in range(len(layers)) :
    plt.loglog(A, Fr[i], label=str(layers[i]))


plt.title("Dowell's Curves")
plt.xlim(A[0], A[-1])
plt.ylim(1., 1000. )
plt.xlabel(r'$h/\delta_w$', fontsize=14)
plt.ylabel(r"$F_R$", fontsize=14)
plt.legend(title='layers')
plt.grid(which='both')
plt.savefig('dowells_curve.png')    
plt.show()

    