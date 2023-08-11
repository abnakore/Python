from PIL import Image
file = "clue.bmp"

imageObject = Image.open(file)
imageObject.show()

for x in range(imageObject.size[0]):
    for y in range(imageObject.size[1]):
        r, g, b = imageObject.getpixel((x, y))
        if r == 255 and b + g == 0:
            imageObject.putpixel((x, y), (220, 255, 220))

imageObject.show()