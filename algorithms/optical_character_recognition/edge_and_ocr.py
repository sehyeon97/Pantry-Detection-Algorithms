import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('algorithms/optical_character_recognition/cabinet_test_1.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
edges = cv.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()

import cv2
import matplotlib.pyplot as plt

# Read an image from file
img = cv2.imread('algorithms/optical_character_recognition/cabinet_test_1.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Canny edge detector
edges = cv2.Canny(img, 100, 200)

# Display the original and edge-detected images
plt.imshow(edges, cmap='gray')
plt.axis('off')

# Save the edge detection image
plt.savefig('edge_image.jpg', bbox_inches='tight', pad_inches=0)

# Show the edge detection image
plt.show()


import cv2
from PIL import Image
import matplotlib.pyplot as plt
import easyocr

reader = easyocr.Reader(['ch_sim','en'], gpu = False)
from PIL import Image
import matplotlib.pyplot as plt
result = reader.readtext('algorithms/optical_character_recognition/edge_image.jpg',detail=0)
print(result)