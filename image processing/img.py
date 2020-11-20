from PIL import Image

image = Image.open("img.png")

# image.show()

# https://pillow.readthedocs.io/en/stable/reference/Image.html?highlight=crop#PIL.Image.Image.crop
# https://pillow.readthedocs.io/en/stable/reference/Image.html?highlight=crop#PIL.Image.Image.getbbox
# https://pillow.readthedocs.io/en/stable/_modules/PIL/Image.html#Image.crop

(left, upper, right, lower) = (20, 20, 100, 100)
cropped = image.crop((left, upper, right, lower))

# https://pillow.readthedocs.io/en/stable/reference/Image.html?highlight=save#PIL.Image.Image.save
filepath = "C:/Users/65909/Documents/Github/PythonSandbox/image processing/cropped.png"

cropped.save(filepath, format="png")