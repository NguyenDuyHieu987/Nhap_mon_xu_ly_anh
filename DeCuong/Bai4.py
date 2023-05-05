import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg")
ims = cv2.resize(img, [640, 480])

b, g, r = cv2.split(ims)
# h, w, k = ims.shape
# Igray = np.zeros((h, w), dtype="uint8")
Igray = cv2.cvtColor(ims, cv2.COLOR_BGR2GRAY)

Igray[:, :] = 0.39 * r + 0.5 * g + 0.11 * b
ret, Ib = cv2.threshold(Igray, 0, 255, cv2.THRESH_OTSU)

cv2.imshow("img thresh otsu", Ib)

cv2.waitKey(0)
cv2.destroyAllWindows()
