# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 04:26:07 2024

@author: GerasMk1.1
"""

import pandas as pd
import numpy as np
import h5py

## THEORETICALLY, THIS IS MODIFIABLE TO BE USED WITH ANY COLUMN OF THE DATA
## TO MAKE A Y_ VECTOR

def get_gender_data(excel_file_path):

    df = pd.read_excel(excel_file_path)

    #extract Gender column (contains needed value)
    gender_data = df['Gender'].to_numpy()

    return gender_data

def save_to_hdf5(data, filename):
    with h5py.File(filename, 'w') as hf:
        hf.create_dataset('gender_data', data=data)


excel_file_path = 'data/Diagnostics.xlsx'
gender_data = get_gender_data(excel_file_path)

print(gender_data.shape)

#np.save('gender_data.npy', gender_data)

#hdf5_filename = 'gender_data.h5'
#save_to_hdf5(gender_data, hdf5_filename)