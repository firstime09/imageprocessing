import cv2, glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def segment_grey(dt):
    # im = cv2.imread(dt)
    b, g, r, = cv2.split(dt)
    gray = (b+g+r)/3
    return gray

def segment_RG(dt):
    # im = cv2.imread(dt)
    b, g, r = cv2.split(dt)
    rg = r - g
    return rg

def segment_GR(dt):
    # im = cv2.imread(dt)
    b, g, r = cv2.split(dt)
    gr = g - r
    return gr

path = r"D:\00AllData\UMN IMAGE"
load_img = cv2.imread(path + '/UMN LOGO.jpg', 0)
# load_img = r"D:\00AllData\UMN IMAGE\UMN LOGO.jpg"
# load_img = glob.glob(path + '/UMN LOGO.jpg')

segment_1 = segment_GR(load_img)
segment_2 = segment_RG(load_img)
segment_Gry = segment_grey(load_img)

path = r"D:\00AllData\UMN IMAGE"
# cv2.imwrite(path + '/UMN LOGO_GR.png', segment_1)
# cv2.imwrite(path + '/UMN LOGO_RG.png', segment_2)
# cv2.imwrite(path + '/UMN LOGO_Gray.png', segment_grey(load_img))

equ = cv2.equalizeHist(load_img)
Med_blur = cv2.medianBlur(equ, 5)
cv2.imwrite(path + '/UMN LOGO_MedBlur_3.png', Med_blur)

# image_ORI = mpimg.imread(load_img)
# image_Grey = mpimg.imread(load_img)
# plt.imshow(image_ORI)
# plt.imshow(image_Grey)
# plt.show()


cv2.imshow('im_show', load_img)
cv2.waitkey(0)
cv2.destroyAllWindows()