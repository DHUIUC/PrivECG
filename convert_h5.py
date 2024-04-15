# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 04:44:49 2024

@author: GerasMk1.1
"""

import h5py
import numpy as np

## CONVERT SAVED FILES TO H5PY TO WORK WITH MODEL -- OOPS!

with h5py.File('downsampled_ecg_data.h5', 'r') as hf:
    downsampled_ecg_data = hf['data'][:]

with h5py.File('downsampled_r_wave_masks.h5', 'r') as hf:
    downsampled_r_wave_masks = hf['data'][:]

with h5py.File('downsampled_non_r_wave_masks.h5', 'r') as hf:
    downsampled_non_r_wave_masks = hf['data'][:]

np.save('ecg_data.npy', downsampled_ecg_data)
np.save('r_wave_masks.npy', downsampled_r_wave_masks)
np.save('non_r_wave_masks.npy', downsampled_non_r_wave_masks)

