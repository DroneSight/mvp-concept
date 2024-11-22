# 1. Prepare the data

- Download the `SAR-Ship-Dataset` from https://github.com/CAESAR-Radi/SAR-Ship-Dataset
- Create the following directories:
    1. `images/train`: This is where all the images from the `SAR-Ship-Dataset` training dataset are going.
    2. `images/validations`: This is where all the validation images from sentinel-1 should be located.
    3. `labels`: This is where all the labels from the `SAR-Ship-Dataset` training dataset are going.

# 2. Train the YOLOv11 on Sentinel-1 data

Run `python3 train.py` to train on the sentinel-1 dataset.
