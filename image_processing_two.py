import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')

import skimage.io
import skimage.filters
import skimage.measure
import skimage.segmentation


# Load an example phase image
phase_im = skimage.io.imread('data/HG105_images/noLac_phase_0004.tif')

# Show the image
with sns.axes_style('dark'):
    plt.imshow(phase_im, cmap=plt.cm.viridis)
    plt.show()

# Apply a gaussian blur (scale is much larger than that of bacteria)
im_blur = skimage.filters.gaussian(phase_im, 50)

# Show the blurred image
plt.imshow(im_blur, cmap=plt.cm.viridis)

# Convert the phase image to a float
phase_float = skimage.img_as_float(phase_im)
phase_sub = phase_float - im_blur

# show both:
plt.figure()
plt.imshow(phase_float, cmap = plt.cm.viridis)
plt.title('original')

plt.figure()
plt.imshow(phase_sub, cmap = plt.cm.viridis)
plt.title('subtracted')

# Apply Otsu thresholding
thresh = skimage.filters.threshold_otsu(phase_sub)
seg = phase_sub < thresh

# Show segmentation
plt.close('all')
plt.imshow(seg, cmap=plt.cm.Greys_r)

# Label them
seg_lab, num_cells = skimage.measure.label(seg, return_num=True, background=0)
plt.close()
plt.imshow(seg_lab, cmap=plt.cm.Spectral_r)

# Compute the region properties and extract area of each object
ip_dist = 0.063 # interpixel distance is 63 nm. so this is microns per pixel
props = skimage.measure.regionprops(seg_lab)

# Get the arreas as an array
areas = np.array([prop.area for prop in props])
cutoff = 300

im_cells = np.copy(seg_lab) > 0 #only background and cell objects?
for i, _ in enumerate(areas):
    if areas[i] < cutoff:
        im_cells[seg_lab==props[i].label] = 0

area_filt_lab = skimage.measure.label(im_cells)

plt.figure()
plt.imshow(area_filt_lab, cmap=plt.cm.Spectral_r)
