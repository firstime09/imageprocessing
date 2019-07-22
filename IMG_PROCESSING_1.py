import cv2
import numpy as np
from matplotlib import pyplot as plt

def segment_RG(dt):
    # im = cv2.imread(dt)
    b, g, r = cv2.split(dt)
    rg = r - g
    return rg

img = cv2.imread(r"D:\00AllData\UMN IMAGE\UMN LOGO.jpg")
RG_IMG = segment_RG(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel_1 = np.ones((9,9),np.float32)/25
kernel_2 = np.zeros((200, 250))
dst = cv2.filter2D(img, -1, kernel_2)

blur = cv2.blur(img,(5,5))
Gaus_blur = cv2.GaussianBlur(RG_IMG, (5,5), 0)
Med_blur = cv2.medianBlur(RG_IMG, 5)

plt.subplot(121),plt.imshow(dst),plt.title('Output_1')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(gray),plt.title('Output_2')
plt.xticks([]), plt.yticks([])
plt.show()