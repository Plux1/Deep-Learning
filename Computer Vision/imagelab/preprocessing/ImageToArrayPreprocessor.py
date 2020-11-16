# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 12:17:37 2020

@author: Tajr
"""

from keras.preprocessing.image import img_to_array

class ImageToArrayPreprocessor:
    # Constructor
    def __init__(self, dataFormat=None):
        # Store the data format
        self.dataFormat = dataFormat
        
    # Data format processor
    def image_array_processor(self, image):
        # Process data using keras img_to_array method
        return img_to_array(image, data_format=self.dataFormat)