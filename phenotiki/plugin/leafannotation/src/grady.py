import cv2
import matplotlib.pyplot as plt
import numpy as np
import skimage
from skimage.color import rgb2gray
from skimage.exposure import rescale_intensity
from skimage.segmentation import random_walker

# Generate noisy synthetic data
img = cv2.imread("../src/IMG_2013-09-28_08-00.png")
img = rgb2gray(img)
#img = filters.sobel(img)
#img = filters.gaussian(img)
#alpha = img[:, :, 1]  # extract it
#binary = ~alpha  # invert b/w
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

#data1 = skimage.img_as_float64(alpha, force_copy=False)

#sigma = 0.35
#data1 += np.random.normal(loc=0, scale=sigma, size=data1.shape)
#data1 = rescale_intensity(data1, in_range=(-sigma, 1 + sigma),
                     #    out_range=(-1, 1))

# The range of the binary image spans over (-1, 1).
# We choose the hottest and the coldest pixels as markers.

markers = np.zeros(data.shape, dtype=np.uint)
markers[data < -0.95] = 1
markers[data > 0.95] = 2

#markers1 = np.zeros(data1.shape, dtype=np.uint)
#markers1[data1 < -0.95] = 1
#markers1[data1 > 0.95] = 2

# Run random walker algorithm
labels = random_walker(data, markers, mode='cg_mg')

# Plot results
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(8, 3.2),
                                    sharex=True, sharey=True)
ax1.imshow(data, cmap='gray', interpolation='nearest')
ax1.axis('off')
ax1.set_title('Noisy data')
ax2.imshow(markers, cmap='gray', interpolation='nearest')
ax2.axis('off')
ax2.set_title('Markers')
ax3.imshow(labels, cmap='binary')
ax3.axis('off')
ax3.set_title('Segmentation')

fig.tight_layout()
plt.show()
print(data)
