# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 04:08:54 2024

@author: GerasMk1.1
"""

import h5py
import numpy as np
from tqdm import tqdm

## BASED ON DOWNSAMPLING METHOD PROVIDED IN PRIVECG README.MD FILE
def ResampleLinear1D(original, target_len):
    original = np.array(original, dtype=np.float64)
    index_arr = np.linspace(0, len(original)-1, num=target_len, dtype=np.float64)
    index_floor = np.array(index_arr, dtype=np.int32)  # Round down
    index_ceil = index_floor + 1
    index_rem = index_arr - index_floor  # Remain

    val1 = original[index_floor]
    val2 = original[index_ceil % len(original)]
    interp = val1 * (1.0 - index_rem) + val2 * index_rem
    assert len(interp) == target_len
    return interp

## MODIFIED TO WORK ON ENTIRE DATASET OF SHAPE (N,5000,12)
def downsample_dataset(h5py_filename, target_len=500):
    
    
    new_filename = f"downsampled_{h5py_filename}"
    with h5py.File(h5py_filename, 'r') as hf:
        dataset = hf['data'][:]
    
        #create an empty array to store the downsampled data
        downsampled_data = np.zeros((len(dataset), target_len, dataset.shape[2]), dtype=np.float64)

        #iterate over each sample in the dataset
        for i in tqdm(range(len(dataset))):
            
            #downsample each lead of the ECG signal
            for j in range(dataset.shape[2]):
                downsampled_data[i, :, j] = ResampleLinear1D(dataset[i, :, j], target_len)

        with h5py.File(new_filename, 'w') as new_hf:
            new_hf.create_dataset('data', data=downsampled_data, compression='gzip')

downsample_dataset('ecg_data.h5')
downsample_dataset('r_wave_masks.h5')
downsample_dataset('non_r_wave_masks.h5')