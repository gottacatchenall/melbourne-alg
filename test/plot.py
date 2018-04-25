#! /usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

# ====================================
# filename
# ====================================

file = "RUN.csv"


### Script

data = np.genfromtxt(file, delimiter=',')


plt.scatter(data[0], data[1])
plt.show()

