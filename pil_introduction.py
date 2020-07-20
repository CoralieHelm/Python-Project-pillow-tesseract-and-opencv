#This code is not used by the Course "Python Project pillow, tesseract and opencv.
#Instead this code serves as a "playground" to learn the material presented in the course material.
#We are going to loop over all images in our current dictionary
#(".") represents the current dictionary.

from PIL import Image, ImageFilter
import os


#saving images in different format
try:
    for file in os.listdir("."):
        if file.endswith("jpg"):
            images = Image.open(file)
            #splitting the file name (fn) and file extention (fext)
            fn, fext = os.path.splitext(file)
            #saving the images as png file in a png folder we created before
            images.save("pngs/{}.png".format(fn))
    print("Images have been saved in pngs folder.")
except Exception as e:
    print("An error occured.")
    print(e)

#saving images in different size
size_500 = (500,500)    
try:
    for file in os.listdir("."):
        if file.endswith("jpg"):
            images = Image.open(file)
            fn, fext = os.path.splitext(file)
            images.thumbnail(size_500)
            images.save("500/{}_500{}".format(fn, fext))
    print("Images have been resized.")
except Exception as e:
    print("An error occured.")
    print(e)

#list all jpg pictures
for file in os.listdir("."):
    if file.endswith("jpg"):
        print(file)

#rotating an image
nature1 = Image.open("nature.jpg")
nature1.rotate(90).save("nature_mod.jpg")

#greyscale
nature2 = Image.open("nature2.jpg")
nature2.convert(mode = "L").save("nature_grey.jpg")

#blurring a picture
nature3 = Image.open("nature3.jpg")
nature3.filter(ImageFilter.GaussianBlur()).save("nature3_blur.jpg")
