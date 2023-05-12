"""
Affine transformations

JCA
"""
import cv2
import numpy as np
import random
import math

def affine(im):
    """Perform an affine transformation.
    Preserves collinearity, parallelism as well as 
    the ratio of distances between the points (translation, rotation, scaling).

    Param 
    :im (np.array) : Image to rotate
    
    """
    # Random transformation matrix
    # 2x3 matrix for rotation and translation
    angle = random.random() * np.pi

    M = np.array([
        [math.cos(angle), -math.sin(angle), 0],
        [math.sin(angle), math.cos(angle), 0]])

    return cv2.warpAffine(src=im, M=M, dsize=(im.shape[0], im.shape[1]), borderValue=(255,255,255))