# practice.py by mohammed
import numpy as np

a = np.array([1,2])
b = np.array([3,4,5])
c = b[1:]

if b[a] is c:
    print(True)
else:
    print(False)
print(b[a])
print(c)

"""
import matplotlib.pyplot as plt # for making graphs

import numpy as np

x = np.random.normal(size=1000)
plt.hist(x, density=True, bins=np.linspace(-5, 5, 21)); #use density instead of normed
plt.subplot(3, 3, 3) 
plt.show() # This will show the stored plot
"""
import random

print(random.choice(random.choice([range(0,10)])))

print(random.choice(list([1,2,3,4])))

import numpy 

print(numpy.sum(numpy.random.randint(1,7,(100,10)), axis=0))

