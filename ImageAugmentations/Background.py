"""
Image augmentation for replace background

JCA
"""
import cv2
import numpy as np

from Auxfunc.location import automatic_contour, draw_contour
from Auxfunc.image import show


def blend(im1, im2, alpha):
    """Blend images with alpha image"""
    return alpha*im1 + (1-alpha)*im2

def background(im, bck):
    """Replace image background
    :im (np.array) : Image with foreground
    :bck (np.array) : Background image
    
    return 
    : res (np.array) : replaced background image
    """
    # Get image contour
    hull, hull_area, hull_center = automatic_contour(im, bck=1, convex_hull=False)

    # Create alpha image
    alpha = np.zeros(im.shape)
    cv2.drawContours(image=alpha, contours=[hull], contourIdx=-1, color=(255, 255, 255), thickness=-1)

    bck = cv2.resize(bck, (im.shape[1], im.shape[0])).astype(float)/255
    im = im.astype(float)/255
    alpha = alpha.astype(float)/255

    # Blur image to diffuse white border
    alpha = cv2.erode(alpha, (7,7)) 
    alpha = cv2.GaussianBlur(alpha,(7,7),0)

    res = blend(im, bck, alpha)

    return res
    


if __name__ == '__main__':
    # Test
    impath = '/Users/juanc/Downloads/SASVAR_clear/151.jpg'
    im = cv2.imread(impath)

    bck = cv2.imread('/Users/juanc/Downloads/bck.jpg')


    res = background(im, bck)
    show(res)

    