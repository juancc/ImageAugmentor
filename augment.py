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

from ImageAugmentations.Color import background
from ImageAugmentations.Affine import affine





# Todo
# Background paths need to get location of the repository
BACKGROUND_PATH = 'Assets/Backgrounds'

parser = argparse.ArgumentParser(
                    prog='Data Augmentation',
                    description='Perform image transformations for data augmentation')

parser.add_argument('dataset', help='Path to dataset')
parser.add_argument('-c', '--childs', help='Number of random variations per source file', default=3)
parser.add_argument('-s', '--size', help='Fix square output image size', default=0)
parser.add_argument('-q', '--quality', help='Output file image quality', default=90)
parser.add_argument('-v', '--verbose', help='Show errors', action='store_true')
parser.add_argument('-i', '--identifier', help='Name added to saved images', default='aug')





def augment(path, childs, target_size, quality, verbose, ident):
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
    files = list(Path(path).glob('**/*'))
    for filepath in tqdm(files, total=len(files)):
        err = []
        try:

            im = cv2.imread(str(filepath))

            childs = int(childs)
            for c in range(childs):
                # Affine
                src = affine(im)
                
                # Background replace
                bck_filepath = os.path.join(BACKGROUND_PATH, random.choice(backgrounds))
                bck = cv2.imread(bck_filepath)
                aug = background(src, bck, add_noise=True, flip=True)*255

                out_filename = f'{filepath.name.split(".")[0]} {ident}-{c}.jpg'
                out_filepath = os.path.join(output_dir, out_filename)
                target_size = int(target_size)
                if target_size>0:
                    aug = cv2.resize(aug, ([target_size]*2), interpolation= cv2.INTER_LINEAR)

                cv2.imwrite(out_filepath, aug, [int(cv2.IMWRITE_JPEG_QUALITY), int(quality)])

        except Exception as e:
            if verbose: print(f'Err:{e} in file: {filepath}')
            err.append(str(filepath))





    if err: print(f'Files with error: { ", ".join(err) }')

if __name__ == '__main__':
    args = parser.parse_args()

    augment(args.dataset, args.childs, args.size, args.quality, args.verbose, args.identifier)