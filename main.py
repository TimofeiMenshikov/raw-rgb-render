from view_functions import read_raw
import pyexifinfo as p
import numpy as np
import cv2 
from wb_cct import get_wb_and_cst_img


def print_img_info(metadata):
    
    print("ForwardingMatrix1", metadata["EXIF:ForwardMatrix1"])
    print("ForwardingMatrix2", metadata["EXIF:ForwardMatrix2"])
    print("WhiteBalance", metadata["EXIF:AsShotNeutral"])


file_path = "cc-lamp.dng"
metadata = p.get_json(file_path)[0]

print_img_info(metadata)


img = read_raw("cc-lamp.dng")
wb_and_cst_img = get_wb_and_cst_img(img, metadata, 0.5)


print(wb_and_cst_img)








