#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#
# PROGRAMMER:  aemonge
# DATE CREATED: 12/10/2022
# REVISED DATE:
# PURPOSE: Create a function that retrieves the following 3 command line inputs
#          from the user using the Argparse Python module. If the user fails to
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse, os
from utils import isntHiddenFile

def _dir_path(path):
    if os.path.isdir(path) and isntHiddenFile(path):
        return path
    else:
        raise NotADirectoryError(path)

def _check_model(model):
    if not isinstance(model, str):
        raise TypeError('Model should be  a string')
    model = model.lower()

    aviableModels = ['vgg', 'alexnet', 'resnet']
    if model not in aviableModels:
        raise TypeError('Model should be one of {}'.format(aviableModels))
    return model

def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's
    argparse module to created and defined these 3 command line arguments. If
    the user fails to provide some or all of the 3 arguments, then the default
    values are used for the missing arguments.
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object
    """

    parser = argparse.ArgumentParser(prog='aemonge-image-clasifier', description="Clasify images, to know it they're dogs and what race they are")
    parser.add_argument('--dir', type=_dir_path, default="pet_images")
    parser.add_argument('--arch', default="vgg", type=_check_model)
    parser.add_argument('--dogfile', type=argparse.FileType('r'), default="dognames.txt")

    return parser.parse_args()
