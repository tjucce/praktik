from PIL import Image

image = Image.open('27.9290769,-15.7234258_pano.jpg')
print(f"Original size : {image.size}") # 5464x3640

sunset_resized = image.resize((224, 224))
sunset_resized.save('27.9290769,-15.7234258_pano_trained.jpg')



mywidth = 896

img = Image.open('27.9290769,-15.7234258_pano.jpg')
print(img.size)
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), Image.ANTIALIAS)
img.save('resized.jpg')
print(img.size)
