import os
import imageio
import numpy as np


dir_dims = os.listdir('.')
concat_order = ['VAE.png', 'GAN_gauss.png', 'GAN_unif.png']

pixels_margin = np.ones((224, 1), np.float32)
pixels_margin = np.multiply(pixels_margin, 255.0)


for dir_i in dir_dims:
    image_files = os.listdir(dir_i)

    pixels_array = [imageio.imread(os.path.join(dir_i, file)) for file in concat_order]

    pixels_array.insert(1, pixels_margin)
    pixels_array.insert(3, pixels_margin)

    for pixels in pixels_array:
        print(pixels.shape)

    merged = np.concatenate(pixels_array, axis=1)

    imageio.imwrite('%s.png' % dir_i, merged)
