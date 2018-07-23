from scipy.misc import imsave, imread
import imageio
import numpy as np
import pickle
import tensorflow as tf


# array = imread('23.png')
# array = array.astype(np.float64) / 255.0
array = pickle.load(open('pixels.pickle', 'rb'))
print(array, array.dtype)
print(np.max(array), np.mean(array), np.min(array))
imsave('scipy.png', array)
imageio.imwrite('imageio.png', array)

array2 = imageio.imread('imageio.png')
print(array2)
array3 = array2 / 255.0

print(np.max(np.abs(array - array3)))


imageio.imwrite('new_imageio.png', np.clip(2 * array3 - 1, 0., 1.))
