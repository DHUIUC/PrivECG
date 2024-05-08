# PrivECG

Author: Dillon Harding


## Overview

This repository contains the code for my implementation of PrivECG.

For full information regarding the project, including the original authors, please refer to the `.ipynb` file included in this repository.

## Requirements

The file requirements.txt lists all of the python packages needed as well as their approximate required version number for use in the Jupyter Notebook file. **I would heavily recommend installing these within an anaconda environment**. As stated in the Jupyter Notebook, those who wish to train the model will find it advantageous to install CUDA if they have an NVIDIA or supported GPU. Listed out, the total requirements for this project, including python packages, are:

- python (3.11.7)
- numpy==1.26.4
- pandas==2.1.4
- torch==2.2.2
- tqdm==4.65.0
- scikit-learn==1.3.0
- py-ecg-detectors
- scipy==1.11.4
- similaritymeasures==0.7.0
- frechetdist
- adapt
- keras==2.11.0
- tensorflow==2.12.0
- keras_resnet
- focal-loss==0.0.7
- CUDA (11.8)


## Data

The data for this project is extremely large, thus unable to be added to GitHub due to their file size constraints. The data can downloaded from the following link (UIUC affiliates only): https://uillinoisedu-my.sharepoint.com/:f:/g/personal/dth3_illinois_edu/ElvictAXINZHvxADE2nR9iABtVjkKecGgYVMvrKkkcO5XA?e=xgk9SF

For running the Jupyter Notebook, you need only download the folders "to_model" and "generated". Upon downloading these folders, please place them into the repository folder, as it should be there and is an essential part of the project.

At this point, you can skip to the section **Running the Notebook**. Though, if you wish to reproduce all steps of the process, continue to follow along.

To access the ECG data used, the raw data can be found here attached to the bottom of the paper: https://doi.org/10.6084/m9.figshare.c.4560497


## Pre-Processing

Many helper python files are utilized in preparing the data for use in the Jupyter Notebook file. The end result of this pre-processing is within the to_model folder at the link provided in the Data section. If you wish to construct this data yourself, you can utilize the following python helper methods in the order they appear:

- readFromExcel.py
- readDiagnostics.py
- createMasks.py
- downsample.py
- convert_h5.py

This assumes you have downloaded the data from the paper at the end of the **Data** section. Running these scripts in order will recreate the to_model folder. In executing these scripts, the ECG excel data will be read and stored in a compressed format. 

Similarly, the Diagnostic data associated with the ECG data will be read and stored in a compressed format. Afterwards, masks will be created for the R-wave data and non-r-wave data from the ECG. This is done using scipy's `find_peaks` function. These masks will be stored in a compressed format. This process can be rather memory intensive, high RAM allocation is recommended.

After all data has been stored in the respective compressed formats, the data is then downsampled to fit the necessary requirements for input into the PrivECG model (N, 500, 12). Once this conversion process has finished, the compressed files are stored as numpy arrays.


## Running the Notebook

With the required data downloaded and placed in the same folder as this repository, open the Jupyter Notebook file. You should at this point be able to activate the conda environment which contains all components listed in the **Requirements** section.

With an environment that follows the outlined versioning, you should be able to run each cell of the notebook and receive analytic data. The Notebook itself will contain more granular information regarding each code cell and its involvement.


## Notes

Setting up the environment is one of the most difficult portions, as the original paper and code utilized by the model were created using dated versions of python packages keras and tensorflow. There is a web of dependencies in which you might find it easier to load the Notebook with a separate environment for the proper keras version after training the model using another conda environment with the non-keras dependencies. 


## Acknowledgements / References

1.  Nolin-Lapalme, A., Avram, R. & Julie, H. (2023). PrivECG: generating private ECG for end-to-end anonymization. Proceedings of the 8th Machine Learning for Healthcare Conference, in Proceedings of Machine Learning Research 219:509-528 Available from https://proceedings.mlr.press/v219/nolin-lapalme23a.html

2.  Nolin-Lapalme, A., et al. (2023). privECG. GitHub. [https://github.com/anolinlapalme/privECG](https://github.com/anolinlapalme/privECG)
