'''
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

i = Image.open('/Users/victorious/Desktop/google_logo.jpg')
image_array = np.asarray(i)
plt.imshow(image_array)
print(image_array)
plt.show()
'''

import os
import sys

def  oddNumbers(l, r):
    for i in range(l,r):
        if (i%2!=0):
            print(i)

oddNumbers(2,10)