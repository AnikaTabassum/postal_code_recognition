import cv2

class cutImage:
	def onlyimage(self, filename):
		print("cutImage", filename)
		image = cv2.imread('dataset/binarized/'+filename)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		blur = cv2.medianBlur(gray, 5)
		thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,8)

		kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
		dilate = cv2.dilate(thresh, kernel, iterations=2)
		cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		cnts = cnts[0] if len(cnts) == 2 else cnts[1]
		cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

		for c in cnts:
		    x,y,w,h = cv2.boundingRect(c)
		    ROI = image[y:y+h, x:x+w]
		    cv2.imwrite('dataset/roi/'+filename, ROI)
		    break

		# cv2.imshow('thresh', thresh)
		# cv2.imshow('dilate', dilate)
		# cv2.imshow('ROI', ROI)
		cv2.waitKey()

# cutImage().onlyimage('1_b.jpg1.jpg')