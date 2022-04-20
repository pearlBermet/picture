from PIL import Image

im = Image.open('aa.jpg')

out = im.resize((1080,1080))

with Image.open('aa.jpg'):
    out = out.convert('L')
out = out.rotate(90)
area = (400,400,800,800)
cropped_img = out.crop(area)
cropped_img.show()