import cv2

img= cv2.imread(r"C:\Users\adity\Desktop\mini soft\Screenshot 2021-04-08 163148.png")
cv2.imshow("orignal image ",img)
#grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("orignal image2 ",grey_img)
print(img.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()