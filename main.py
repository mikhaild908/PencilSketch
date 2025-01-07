import cv2
# image = cv2.imread("sonic-01.png")
image = cv2.imread("lauren.jpg")
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted_image = cv2.bitwise_not(grey_image)
blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred_image = cv2.bitwise_not(blurred_image)
sketch = cv2.divide(grey_image, inverted_blurred_image, scale=256.0)

# cv2.imwrite("sketch-01.png", sketch)
cv2.imwrite("lauren-sketch-01.png", sketch)