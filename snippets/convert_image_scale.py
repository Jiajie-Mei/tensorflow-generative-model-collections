import os
import imageio
import numpy as np


dir_dims = os.listdir('.')

for dir_i in dir_dims:
    image_files = os.listdir(dir_i)

    for image_i in image_files:
        if image_i.endswith('.png'):

            path = os.path.join(dir_i, image_i)
            pixels = imageio.imread(path)

            if np.min(pixels) >= 127:

                pixels = pixels / 255.0

                # inverse inverse transformation
                pixels = 2.0 * pixels - 1.0

                pixels = np.clip(pixels, 0.0, 1.0)

                imageio.imwrite(path, pixels)
