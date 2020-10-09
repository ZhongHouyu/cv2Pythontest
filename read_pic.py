import cv2
import numpy as np
from matplotlib import pyplot as plt

origin_img = cv2.imread('test.bmp')
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

B, G, R = cv2.split(origin_img)
ret, B_thresh = cv2.threshold(G, 127, 255, cv2.THRESH_BINARY)
eroded = cv2.erode(B_thresh,kernel)
dilate = cv2.dilate(B_thresh,kernel)
pic = dilate - eroded
plt.imshow(pic)
plt.show()
