# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 02:26:03 2024

@author: GerasMk1.1
"""

import pandas as pd
import numpy as np
import h5py
import os

excel_dir = "data/ECGData"

#Read each CSV in ECGData folder
def read_excel_files_to_array(excel_dir):
    data_arrays = []
    for filename in os.listdir(excel_dir):
        if filename.endswith(".csv"):
            file_path = os.path.join(excel_dir, filename)
            df = pd.read_csv(file_path, skiprows=1)  # Skip header
            data_arrays.append(df.values)
    return np.array(data_arrays)


#Save to HDF5 file
def save_array_to_hdf5(data_array, filename):
    with h5py.File(filename, 'w') as hf:
        hf.create_dataset('data', data=data_array, compression='gzip')
        
        
excel_data_array = read_excel_files_to_array(excel_dir)
save_array_to_hdf5(excel_data_array, 'ecg_data.h5')

