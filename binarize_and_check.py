import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import sys
np.set_printoptions(threshold=sys.maxsize)
import csv
class binarize:
	def checkImage(self,filename):
		csvFileName='dataset/csv/'+filename+'.csv'
		with open(csvFileName, 'w', newline='') as file:
			writer = csv.writer(file)
			writer.writerow(["imageNo", "value"])
			try:
				for i in range(1,7):
					print("filename", filename)
					# img = cv.imread('dataset/cropped_and_resized/rakib_hdr_'+str(3)+'.jpg',0)
					img= cv.imread("dataset/segmented/"+filename+str(i)+".png",0)
					height, width = img.shape

					print("height ", height, "width", width)
					dim= (65,45)
					img = cv.resize(img, dim, interpolation = cv.INTER_AREA)
					img2= img[5:40,10:55]
					# global thresholding
					ret1,th1 = cv.threshold(img,0,255,cv.THRESH_BINARY)
					# Otsu's thresholding
					ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
					ret99,th99 = cv.threshold(img2,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
					# Otsu's thresholding after Gaussian filtering
					blur = cv.GaussianBlur(img,(5,5),0)
					ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
					# plot all the images and their histograms
					images = [img, 0, th1,
										img, 0, th2,
										img2, 0, th99]
					# cv.imshow("otsu", th2)
					cv.imwrite('dataset/binarized/'+filename+str(i)+".jpg", th2)
					print("th99 ", len(th99), type(th99), np.sum(th99), np.count_nonzero(th99==0))
					writer.writerow([str(i), np.count_nonzero(th99==0)])
					# titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
					# 					'Original Noisy Image','Histogram',"Otsu's Thresholding",
					# 					'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
					# for i in range(3):
					# 		plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
					# 		plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
					# 		plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
					# 		plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
					# 		plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
					# 		plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
					# plt.show()
			except Exception as e:
				print("filenai")

		return csvFileName


# binarize().checkImage("2_b.jpg")