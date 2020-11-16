# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 11:51:04 2020

@author: Tajr
"""

import cv2

class ImageResizePreprocessor:
    # Constructor
    def __init__(self, width, height, inter=cv2.INTER_AREA):
        # Store the target image width, height and interpolation method used when resizing
        self.width = width
        self.height = height
        self.inter = inter
    
    # Size Processor
    def resize_processor(self, image):
        # Resize image while ignoring the aspect ratio
        return cv2.resize(image, (self.width, self.height), interpolation=self.inter)