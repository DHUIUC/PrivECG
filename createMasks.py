# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 02:47:21 2024

@author: GerasMk1.1
"""

import numpy as np
from scipy.signal import find_peaks
import h5py

## GENERATE R-WAVE INDICES FOR EACH LEAD IN THE GIVEN ECG SIGNAL
def generate_r_wave_indices(ecg_signal):
    r_wave_indices = []
    for lead in ecg_signal.T:  # Iterate over each lead
        peaks, _ = find_peaks(lead, height=0)  # Find peaks in the lead signal
        r_wave_indices.append(peaks)
    return r_wave_indices

## GENERATE R-WAVE MASK BASED ON R-WAVE INDICES
def generate_r_wave_mask(ecg_signal, r_wave_indices):
    #print(np.array(r_wave_indices).shape)
    r_wave_mask = np.zeros_like(ecg_signal)
    flat_indices = np.concatenate(r_wave_indices)
    r_wave_mask[flat_indices] = 1
    return r_wave_mask

## GENERATE NON-R-WAVE MASK BASED ON R-WAVE MASK
def generate_non_r_wave_mask(ecg_signal, r_wave_mask):
    non_r_wave_mask = np.ones_like(ecg_signal)
    non_r_wave_mask[r_wave_mask == 1] = 0
    return non_r_wave_mask

## LOAD ECG DATA FROM H5PY
def load_ecg_data_from_hdf5(filename):
    with h5py.File(filename, 'r') as hf:
        ecg_data = hf['data'][:]
    return ecg_data

## SAVE DATA TO H5PY 
def save_array_to_hdf5(data_array, filename):
    with h5py.File(filename, 'w') as hf:
        hf.create_dataset('data', data=data_array, compression='gzip')




## HAD TO SEPARATE THESE OUT FOR MEMORY CONCERNS
## COMMENT / UNCOMMENT AS NECESSARY


#load ECG data from HDF5 file
ecg_data = load_ecg_data_from_hdf5('ecg_data.h5')

## FOR R-WAVE
#all_r_wave_indices = []
#all_r_wave_masks = []


#Generate R-Wave Mask
#for ecg_signal in ecg_data:
        
    #Generate R-wave indices
    #r_wave_indices = generate_r_wave_indices(ecg_signal)
    #all_r_wave_indices.append(r_wave_indices)
    
    #Generate R-wave mask
    #r_wave_mask = generate_r_wave_mask(ecg_signal, r_wave_indices)
    #all_r_wave_masks.append(r_wave_mask)
    
    #Generate non-R-wave mask
    #non_r_wave_mask = generate_non_r_wave_mask(ecg_signal, r_wave_mask)
    #all_non_r_wave_masks.append(non_r_wave_mask)
    
## SAVE R-WAVE MASKS
#save_array_to_hdf5(np.array(all_r_wave_masks), 'r_wave_masks.h5')



## FOR NON-R-WAVE

all_r_wave_masks = load_ecg_data_from_hdf5('r_wave_masks.h5')
all_non_r_wave_masks = []

for r_wave_mask, ecg_signal in zip(all_r_wave_masks, ecg_data):
    
    non_r_wave_mask = generate_non_r_wave_mask(ecg_signal, r_wave_mask)
    all_non_r_wave_masks.append(non_r_wave_mask)
    
## SAVE NON-R-WAVE MASKS
save_array_to_hdf5(np.array(all_non_r_wave_masks), 'non_r_wave_masks.h5')