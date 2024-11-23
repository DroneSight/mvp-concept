import os
import random
import shutil
from pathlib import Path

import yaml

dataset_name = "sar-ships"
classes_file = "classes.txt"

dataset_dir = "ship_dataset_v0"
train_dir = "train"
test_dir = "test"
val_dir = "val"
dirs = (train_dir, test_dir, val_dir)
probabilities = {
    train_dir: 0.6,
    test_dir: 0.2,
    val_dir: 0.2
}

annotation_output_dirs_name = 'labels'
images_output_dirs_name = 'images'

with open(classes_file) as file:
    classes = {value: key for key, value in dict(enumerate(file)).items()}


for directory in dirs:
    directory = Path(dataset_dir) / directory
    os.mkdir(directory)
    os.mkdir(directory / images_output_dirs_name)
    os.mkdir(directory / annotation_output_dirs_name)

no_extension_filenames = {filename.split('.')[0] for filename in os.listdir(dataset_dir)} - set(dirs)
for filename in no_extension_filenames:
    directory = random.choices(list(probabilities.keys()), list(probabilities.values()))[0]

    old_image_path = Path(dataset_dir) / (filename + '.jpg')
    new_image_path = Path(dataset_dir) / directory / images_output_dirs_name / (filename + '.jpg')
    old_annotation_path = Path(dataset_dir) / (filename + '.txt')
    new_annotation_path = Path(dataset_dir) / directory / annotation_output_dirs_name / (filename + '.txt')

    shutil.move(old_image_path, new_image_path)
    shutil.move(old_annotation_path, new_annotation_path)

data = {
    'path': '../' + dataset_dir,
    'train': train_dir,
    'test': test_dir,
    'val': val_dir,
    'names': {value: key for key, value in classes.items()}
}

with open(dataset_name + '.yaml', 'w') as file:
    yaml.dump(data, file)
