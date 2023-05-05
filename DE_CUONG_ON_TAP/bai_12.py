
# 12 Chuyển đổi ảnh I sang ảnh HSV được ma trận ảnh Ihsv. 
# Hiển thị kênh S của ảnh Ihsv

import cv2
import numpy as np

I = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh1.jpg", 1)
# I=cv2.resize(I, (400, 200))
cv2.imshow("anh goc", I)

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow("anh hsv", Ihsv)

h,s,v = cv2.split(Ihsv)
cv2.imshow("anh kenh S", s)
# cv2.imshow("anh kenh S khong dung split", Ihsv[:,:,1])

cv2.waitKey(0)
cv2.destroyAllWindows()