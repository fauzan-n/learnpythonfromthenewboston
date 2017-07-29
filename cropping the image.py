from PIL import Image

img = Image.open("D:\Pictures\wallpaper\cropthis.jpg")

area = (50,50,300,300)
croppedimg = img.crop(area)

croppedimg.show()