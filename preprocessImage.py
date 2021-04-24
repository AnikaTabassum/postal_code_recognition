# make a prediction for a new image.
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from tensorflow.keras.models import *
import numpy as np
import os
from crop_and_resize import cropResize
from segment_image import segmentation
from binarize_and_check import binarize
from find_white_image import findWhiteImage
from predict_digit import predictDigit
from cut_the_image import cutImage
# load and prepare the image
class preprocessImage:
	def readyImage(self, filename):
		cropResize().crop_image(filename)
		segmentation().segment_the_image(filename)

	def detectWhiteImage(self, filename):
		csvFileName=binarize().checkImage(filename)
		whiteImageNos=findWhiteImage().get_image_no(csvFileName)
		postalCode=""
		for i in range(1,7):
			try:
				if i not in whiteImageNos:
					imageName= filename+str(i)+".jpg"
					cutImage().onlyimage(imageName)
					digit=predictDigit().run_example(imageName)
					postalCode= postalCode+str(digit)
				
			except Exception as e:
				print("nainai")

		return postalCode
	
# for i in range(0,10):
# 	imageName="D:\\8th_semester\\my_8th_semester\\Machine_Learning\\bangla_handwritten_digit_recognition\\Photos\\"+str(i)+"_converted"+".jpg"
# 	result=predictDigit().run_example(imageName)

# 	print("                "+str(i)+ " is predicted as "+ str(result))
filename= "2_a.jpg"
preprocessImage().readyImage(filename)
postalCode=preprocessImage().detectWhiteImage(filename)
print("Postal Code for this image is : ", postalCode)