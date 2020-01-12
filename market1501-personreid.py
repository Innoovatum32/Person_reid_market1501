import cv2
from reid import reid
import matplotlib.pyplot as plt
from imageio import imread
im1 = cv2.cvtColor(cv2.imread('path/to/your/folder/img001.png'), cv2.COLOR_BGR2RGB)
im2 = cv2.cvtColor(cv2.imread('path/to/your/folder/img002.png'), cv2.COLOR_BGR2RGB)
model = reid.ReId()
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(121); ax.axis('off')
ax.imshow(im1)
ax = fig.add_subplot(122); ax.axis('off')
ax.imshow(im2)
plt.show()