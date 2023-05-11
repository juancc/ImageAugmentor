"""
Image auxiliar functions

JCA
"""
import cv2

def show(im, window='window'):
    """Shortcut for display image with Opencv"""
    cv2.imshow(window,im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()