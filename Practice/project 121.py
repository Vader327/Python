import cv2
import numpy as np

cap = cv2.VideoCapture(0)
image = cv2.imread("hotel_room.jpg") 
  
while (cap.isOpened()):
  ret, frame = cap.read()

  frame = cv2.resize(frame, (640, 480)) 
  image = cv2.resize(image, (640, 480)) 

  if not ret:
    break
  
  frame = np.flip(frame, axis=1)

  upper_black = np.array([110, 110, 110], np.uint8) 
  lower_black = np.array([0, 0, 0], np.uint8)
  mask = cv2.inRange(frame, lower_black, upper_black)
  res = cv2.bitwise_and(frame, frame, mask=mask)

  rows,cols,channels = res.shape
  roi = image[0:rows, 0:cols ]

  # Now create a mask of logo and create its inverse mask also
  img2gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
  ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
  mask_inv = cv2.bitwise_not(mask)

  # Now black-out the area of logo in ROI
  img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

  # Take only region of logo from logo image.
  img2_fg = cv2.bitwise_and(res,res,mask = mask)

  # Put logo in ROI and modify the main image
  dst = cv2.add(img1_bg,img2_fg)
  image[0:rows, 0:cols ] = dst
  
  cv2.imshow("Output", image)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
