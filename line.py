import cv2 
import numpy as np 

def show(img):
	cv2.imshow('FRAME', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

#read from camera
cap = cv2.VideoCapture(0)
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
	print("Error opening video stream or file")
 
# Read until video is completed
while(cap.isOpened()):
	# Capture frame-by-frame
	ret, frame = cap.read()
	if ret == True:
		# Convert the img to grayscale 
		gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		# Apply edge detection method on the image 
		edges = cv2.Canny(gray,50,150,apertureSize = 3)

		# This returns an array of r and theta values 
		lines = cv2.HoughLines(edges,1,np.pi/180, 100)
		print(lines)
		print(lines.shape)

		for r,theta in lines[0]:
			print('check')
			
			# Stores the value of cos(theta) in a 
			a = np.cos(theta) 

			# Stores the value of sin(theta) in b 
			b = np.sin(theta) 
			
			# x0 stores the value rcos(theta) 
			x0 = a*r 
			
			# y0 stores the value rsin(theta) 
			y0 = b*r 
			
			# x1 stores the rounded off value of (rcos(theta)-1000sin(theta)) 
			x1 = int(x0 + 1000*(-b)) 
			
			# y1 stores the rounded off value of (rsin(theta)+1000cos(theta)) 
			y1 = int(y0 + 1000*(a)) 

			# x2 stores the rounded off value of (rcos(theta)+1000sin(theta)) 
			x2 = int(x0 - 1000*(-b)) 
			
			# y2 stores the rounded off value of (rsin(theta)-1000cos(theta)) 
			y2 = int(y0 - 1000*(a)) 
			
			# cv2.line draws a line in img from the point(x1,y1) to (x2,y2). 
			# (0,0,255) denotes the colour of the line to be 
			#drawn. In this case, it is red. 
			cv2.line(frame,(x1,y1), (x2,y2), (0,0,255),5)

		# Display the resulting frame
		cv2.imshow('Frame',frame)

		# Press Q on keyboard to  exit
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break
	
	else: 
		break

# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()
	
	
	
	
	
	

# Reading the required image in 
# which operations are to be done. 
# Make sure that the image is in the same 
# directory in which this python program is 
#img = cv2.imread('7.jpg') 



# The below for loop runs till r and theta values 
# are in the range of the 2d array 
		 
	
# All the changes made in the input image are finally 
# written on a new image houghlines.jpg 
#cv2.imwrite('linesDetected.jpg', img) 

