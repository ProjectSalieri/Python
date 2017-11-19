from PIL import Image

filename = "GoogleIcon.png"

img = Image.open(filename)

width, height = img.size
for x in range(width):
    img.putpixel((x, 0), (0, 0, 0))

img.show()
img.save("./OuputTest.png")
