"""
Affine transformations

JCA
"""
import cv2
import numpy as np
import random
import math

def affine(im, max_angle=360):
    """Perform an affine transformation.
    Preserves collinearity, parallelism as well as 
    the ratio of distances between the points (translation, rotation, scaling).

    Param 
    :im (np.array) : Image to rotate
    """
    # Scale for width and height deformation
    sy = max(random.random()*2,0.4)
    im = cv2.resize(im, None, fx=1, fy=sy, interpolation= cv2.INTER_LINEAR)


    # Translate image to center to rotate 
    w = im.shape[0]
    h = im.shape[1]
    cx = w/2
    cy = h/2

    # Rotate and scale
    angle = random.randrange(0,max_angle)
    scale = max(random.random(),0.2)
    M = cv2.getRotationMatrix2D((cx, cy), angle, scale)
    im = cv2.warpAffine(im, M, (w, h), borderValue=(255,255,255))

    # Translate
    dx = random.randrange(-w, w)/4
    dy = random.randrange(-h, h)/4

    T = np.array([[1,0, dx],
                  [0,1, dy]])
    im = cv2.warpAffine(im, T, (w, h), borderValue=(255,255,255))


    return im