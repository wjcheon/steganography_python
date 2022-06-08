# python moudle
from LSBSteg import LSBSteg
import numpy as np
import cv2
import os
import string

path_folder = r"C:\Users\wjcheon\Downloads\여성"
dirList  = []

for path_temp in os.listdir(path_folder):
    if os.path.isdir(os.path.join(path_folder, path_temp)):
        dirList.append(path_temp)
        dirFullPathTemp = os.path.join(path_folder, path_temp)
        dirFullPathTemp_steg = path_temp +'_steg_text'
        if not os.path.exists(dirFullPathTemp_steg):
            os.mkdir(dirFullPathTemp_steg) # current code location
        for file_temp in os.listdir(dirFullPathTemp):
            # steganography
            file_temp_fulldir = os.path.join(dirFullPathTemp, file_temp)
            img_array = np.fromfile(file_temp_fulldir, np.uint8)
            img_original = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            # img_original = cv2.imread(r"original_image.jpg")
            data = open(r"backgournd_image.png", "rb").read()
            # cv2.imshow('Original image', img_original)
            # cv2.waitKey(0)
            # cv2.destroyWindow()

            steg = LSBSteg(img_original)
            # # # image steganography: binary method
            # new_img = steg.encode_binary(data)
            new_img = steg.encode_text("All rights are reserved to us")
            filename_split_temp = file_temp.split('.')
            filename_new = filename_split_temp[0]+".png"
            result, encoded_new_img = cv2.imencode('.png', new_img)
            if result:
                with open(os.path.join(dirFullPathTemp_steg, filename_new), mode='w+b') as f:
                    encoded_new_img.tofile(f)

                    # decoding
                    deconding_filename = os.path.join(dirFullPathTemp_steg, filename_new)
                    img_array_decode = np.fromfile(deconding_filename, np.uint8)
                    img_decode = cv2.imdecode(img_array_decode, cv2.IMREAD_COLOR)

                    steg = LSBSteg(img_decode)
                    # # # image steganography: binary method
                    # binary = steg.decode_binary()
                    # img_decode_name = filename_split_temp[0]+"_decoded.png"
                    # with open(os.path.join(dirFullPathTemp_steg, img_decode_name), "wb") as f:
                    #     f.write(data)
                    # f.close()

                    binary = steg.decode_text()
                    print(binary)


