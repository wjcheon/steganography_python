# python moudle 
from LSBSteg import LSBSteg
import numpy as np
import cv2
## Text (working)
#encoding
img_original = cv2.imread(r"original_image.png")
cv2.imshow('Original image', img_original)
steg = LSBSteg(img_original)
img_encoded = steg.encode_text("All rights are reserved to the WEKNEW")
cv2.imwrite("my_new_image.png", img_encoded)

#decoding
im = cv2.imread(r"my_new_image.png")
steg = LSBSteg(im)
print("Text value:",steg.decode_text())


##image steganography (not working)
# img_original = cv2.imread(r"original_image.png")
img_original = np.zeros((400,400,3), np.uint8)
img_background = cv2.imread(r"backgournd_image.png")
img_background_resz = cv2.resize(img_background, (200, 200), interpolation=cv2.INTER_CUBIC)

cv2.imshow('Original image', img_original)
cv2.imshow('Backgournd image', img_background_resz)

steg = LSBSteg(img_original)
new_im = steg.encode_image_mod(img_background_resz)
cv2.imshow('New image', new_im)
cv2.imwrite("new_image.png", new_im)


#decoding
img_new = cv2.imread(r"new_image.png")
print(np.sum(new_im-img_new))
print(np.sum(img_original-img_new))
steg = LSBSteg(img_new)
img_decoded = steg.decode_image()
# cv2.SaveImage("recovered.png", img_decoded)
cv2.imshow('Decoded (hide) image', img_decoded)

## Binary steganography (working: png)
#encoding
img_original = cv2.imread(r"original_image.png")
data = open(r"backgournd_image.png", "rb").read()
cv2.imshow('Original image', img_original)

steg = LSBSteg(img_original)
new_img = steg.encode_binary(data)
cv2.imwrite("new_image-3.png", new_img)

#decoding
steg = LSBSteg(cv2.imread("new_image-3.png"))
binary = steg.decode_binary()
with open("recovered-3.png", "wb") as f:
    f.write(data)
f.close()