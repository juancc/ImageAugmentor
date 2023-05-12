"""
Perform image transformations for data augmentation. 
Works better with a perfect white color background images.

Backgrounds included in the repository from:
https://www.kaggle.com/datasets/lprdosmil/unsplash-random-images-collection

Augmentations:
 - Random Background 

JCA
"""
import argparse
from pathlib import Path
import os
import random

import cv2
from tqdm import tqdm

from ImageAugmentations.Background import background
from ImageAugmentations.Affine import affine





# Todo
# Background paths need to get location of the repository
BACKGROUND_PATH = 'Assets/Backgrounds'

parser = argparse.ArgumentParser(
                    prog='Data Augmentation',
                    description='Perform image transformations for data augmentation')

parser.add_argument('dataset', help='Path to dataset')
parser.add_argument('-c', '--childs', help='Number of random variations per source file', default=3) 

def augment(path, childs):
    """
    : path (Str) : path to dataset
    """
    print(' - Data augmentation - ')

    # Creating output directory
    # In the same path of the directory create a folder with the same name plu -aug
    data_name = path.split(os.sep)[-1]+'-aug'
    output_dir = os.path.join(os.sep.join(path.split(os.sep)[:-1]), data_name)
    os.makedirs(output_dir, exist_ok=True)
    print(f'    - Output directory: {output_dir}')

    backgrounds = os.listdir(BACKGROUND_PATH)

    for filepath in tqdm(Path(path).glob('**/*')):
        err = []
        # try:

        im = cv2.imread(str(filepath))

        for c in range(childs):
            # Affine
            src = affine(im)
            


            # Background replace
            bck_filepath = os.path.join(BACKGROUND_PATH, random.choice(backgrounds))
            bck = cv2.imread(bck_filepath)
            aug = background(src, bck)*255


            out_filepath = os.path.join(output_dir, filepath.name+f'-{c}.png')
            cv2.imwrite(out_filepath, aug)


        return

        # except Exception as e:
        #     err.append(str(filepath))





    if err: print(f'Files with error: { ", ".join(err) }')

if __name__ == '__main__':
    args = parser.parse_args()

    augment(args.dataset, args.childs)