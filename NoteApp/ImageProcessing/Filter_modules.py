#Import required Image library
from PIL import Image, ImageFilter

#Open existing image
OriImage = Image.open('simBlurImage.jpg')
OriImage.show()

blurImage = OriImage.filter(ImageFilter.BLUR)
blurImage.show()
#Save blurImage
blurImage.save('simBlurImage.jpg')