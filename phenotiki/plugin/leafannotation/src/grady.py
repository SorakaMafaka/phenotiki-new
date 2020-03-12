import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.segmentation import random_walker
from skimage.data import binary_blobs
from skimage.exposure import rescale_intensity
import skimage
import cv2

# Generate noisy synthetic data
img = cv2.imread(
    'C:\\Users\\SorakaMafaka\\PycharmProjects\\Phenotiki\\phenotiki\\plugin\\leafannotation\\src\\IMG_2013-09-28_08' \
    '-00.png ', -1)
alpha = img[:, :, 2]  # extract it
binary = ~alpha  # invert b/w
# cv2.imshow("Gay", img)
cv2.waitKey()

# blank_image = np.zeros((128, 128, 3), np.uint8)
# blank_image[:,0:128//2] = (255,0,0)
# blank_image[:,0:128//2:128] = (0,255,0)
# skimage.io.imread

data = skimage.img_as_float64(img, force_copy=False)

sigma = 0.35
data += np.random.normal(loc=0, scale=sigma, size=data.shape)
data = rescale_intensity(data, in_range=(-sigma, 1 + sigma),
                         out_range=(-1, 1))

data1 = skimage.img_as_float64(alpha, force_copy=False)

sigma = 0.35
data1 += np.random.normal(loc=0, scale=sigma, size=data1.shape)
data1 = rescale_intensity(data1, in_range=(-sigma, 1 + sigma),
                         out_range=(-1, 1))

# The range of the binary image spans over (-1, 1).
# We choose the hottest and the coldest pixels as markers.

markers = np.zeros(data1.shape, dtype=np.uint)
markers[data1 < -0.95] = 1
markers[data1 > 0.95] = 2

#markers1 = np.zeros(data1.shape, dtype=np.uint)
#markers1[data1 < -0.95] = 1
#markers1[data1 > 0.95] = 2

# Run random walker algorithm
labels = random_walker(data1, markers, mode='cg_mg')

# Plot results
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(8, 3.2),
                                    sharex=True, sharey=True)
ax1.imshow(data, cmap='gray')
ax1.axis('off')
ax1.set_title('Noisy data')
ax2.imshow(markers, cmap='magma')
ax2.axis('off')
ax2.set_title('Markers')
ax3.imshow(labels, cmap='gray')
ax3.axis('off')
ax3.set_title('Segmentation')

fig.tight_layout()
plt.show()
print(data)
