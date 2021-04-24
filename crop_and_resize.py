# Improting Image class from PIL module
from PIL import Image
import os
class cropResize:
	def crop_image(self, filename):
		fullFileName=os.getcwd()+"/dataset/mainImage/"+ filename
		# im = Image.open(r"dataset/rakib_hdr_"+str(i)+".jpg")
		im = Image.open(fullFileName)
		# Size of the image in pixels (size of orginal image)
		# (This is not mandatory)
		width, height = im.size
		print("width ", width , "height", height)
		# Setting the points for cropped image
		# The crop method from the Image module takes four coordinates as input.
		# The right can also be represented as (left+width)
		# and lower can be represented as (upper+height).
		(left, upper, right, lower) = (width- (0.5* width), height - (0.25* height), width- (width*0.015), height- (height*0.08))
		im1 = im.crop((left, upper, right, lower))
		newsize = (700,200)
		im1 = im1.resize(newsize)
		# im1= im1.convert('L')
		# Shows the image in image viewer
		im1.show()
		im1 = im1.save(os.getcwd()+"/dataset/cropped_and_resized/"+filename)

# cropResize().crop_image("2_a.jpg")