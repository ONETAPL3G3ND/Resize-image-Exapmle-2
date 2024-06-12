#https://github.com/ONETAPL3G3ND
import cv2 
src = cv2.imread('D:/cv2-resize-image-original.png', cv2.IMREAD_UNCHANGED) 
# set a new width in pixels 
new_width = 300 
# dsize 
dsize = (new_width, src.shape[0]) 
# resize image 
output = cv2.resize(src, dsize, interpolation = cv2.INTER_AREA) 
cv2.imwrite('D:/cv2-resize-image-width.png',output)
