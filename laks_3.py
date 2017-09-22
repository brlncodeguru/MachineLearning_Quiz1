#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 10:53:20 2017

@author: lakshminarayanabr
"""

import numpy as np


#3(2) Calculating eigen value and eigen vector
a = np.array([[0, -1],[2, 3]])

eigenvalues = np.linalg.eigvals(a)

eigvec = np.linalg.eig(a)

print eigenvalues

print eigvec