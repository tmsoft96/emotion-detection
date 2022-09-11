import cv2
import numpy as np

# importing and reading images
img = cv2.imread("assets/Ryan Reynolds.jpg")
kernel = np.ones((5,5), np.uint8)

# resizing image

# print the sizes
print(img.shape)
imgResize = cv2.resize(img, (300, 300))

# cropping image
imgCropped = img[0:100, 150:250]

#  drawing shape on image
cv2.line(imgResize, (0,0), (imgResize.shape[1], imgResize.shape[0]), (0,255,0), 3)
cv2.rectangle(imgResize, (0,0), (230, 230), (0,0,255), 3)
cv2.circle(imgResize, (200, 50), 30, (255,255,0), 5)
cv2.putText(imgResize, "Michael", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,150,0), 3)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)

#detecting edge in image
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgErode = cv2.erode(imgDialation, kernel, iterations=1)

# output
# cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
# cv2.imshow("Image Cropped", imgCropped)
# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Blue Image", imgBlur)
# cv2.imshow("Canny Image", imgCanny)
# cv2.imshow("Dialation Image", imgDialation)
# cv2.imshow("Erode Image", imgErode)
cv2.waitKey(0)