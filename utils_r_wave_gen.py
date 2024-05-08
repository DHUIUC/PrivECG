# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:05:50 2024

@author: GerasMk1.1
"""

from tqdm import tqdm
import numpy as np
from ecgdetectors import Detectors
detectors = Detectors(50)


data_path = 'to_model/ecg_data.npy'
dataset = np.load(data_path)

save_path = 'to_model'

list_data_R_wave = []
list_data_non_R_wave = []

for ECG in tqdm(dataset, desc="Processing dataset"):
    r_peaks = detectors.christov_detector(ECG[1])  # Assuming ECG[1] contains lead 1 data

    # Create mask for R waves
    l_empty = []
    for i in r_peaks:
        l_empty += list(range(i - 5, i + 6))

    list_dummy = np.zeros(500)
    list_dummy[l_empty] = 1
    list_data_R_wave.append(list_dummy)
    list_data_non_R_wave.append(1 - list_dummy)

# Convert lists to numpy arrays
array_data_R_wave = np.array(list_data_R_wave)
array_data_non_R_wave = np.array(list_data_non_R_wave)

# Save the numpy arrays
np.save(save_path + "_R_wave.npy", array_data_R_wave)
np.save(save_path + "_non_R_wave.npy", array_data_non_R_wave)