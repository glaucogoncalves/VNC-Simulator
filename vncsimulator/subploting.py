"""Examples illustrating the use of plt.subplots().
"""

import matplotlib.pyplot as plt
import numpy as np

# Simple data to display in various forms
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

# 1a forma de fazer: dois subplots em linhas com array 
f, axarr = plt.subplots(2, sharex=True)
axarr[0].set_title('graf1')
axarr[0].plot(x, y)
axarr[0].set_title('graf2')
axarr[1].plot(x, y)

# 2a forma de fazer: dois subplots em colunas com array ja desempacotado
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.set_title('graf1')
ax1.plot(x, y)
ax2.set_title('graf2')
ax2.plot(x, y)

plt.show()