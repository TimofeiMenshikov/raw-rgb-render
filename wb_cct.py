from view_functions import read_raw
import pyexifinfo as p
import cv2 
import numpy as np


def get_wb_matrix_ELIF(metadata):
    
    return np.diag(list(map(float, metadata["EXIF:AsShotNeutral"].split(' '))))


def get_T_matrix_ELIF(metadata):
    
    T1_list = list(map(float, metadata["EXIF:ForwardMatrix1"].split(' ')))
    T2_list = list(map(float, metadata["EXIF:ForwardMatrix2"].split(' ')))

    T1 = np.array([T1_list[0:3], T1_list[3:6], T1_list[6:9]])
    T2 = np.array([T2_list[0:3], T2_list[3:6], T2_list[6:9]])

    return (T1, T2)


def get_T_matrix_from_interpolation(metadata, g):

    T1, T2 = get_T_matrix_ELIF(metadata)

    return T1 * g + T2 * (1 - g)


def get_2D_img_matrix(img):

    return img.reshape(len(img) * len(img[0]), 3)



def get_wb_and_cst_img(img, metadata, g):

    return get_2D_img_matrix(img) @ get_T_matrix_from_interpolation(metadata, g) @ get_wb_matrix_ELIF(metadata) 
