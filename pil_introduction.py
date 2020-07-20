from PIL import Image
import os
print(os.getcwd())
print(os.listdir())

try:
    nature_pic = Image.open("nature3.jpg")
    nature_pic.show()

except Exception as e:
    print("An error happen. The image could not load.")
