#try:
#	file = open ("D:/godzilla.jpg")
#import PIL
from PIL import Image
try:
	pt = input()
	im = Image.open (pt)
	im.show()
#im = Image.open ("D:/godzilla.jpg")
except Exception:
	print("Please enter valid filepath and filename")
#finally:
#	print("Thank You!")
