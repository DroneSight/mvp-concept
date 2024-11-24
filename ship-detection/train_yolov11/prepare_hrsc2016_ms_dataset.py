import json
import os
import shutil
from pathlib import Path

import yaml

dataset_name = "hrsc2016-ms"
classes_file = "classes.txt"

dataset_dir = "hrsc2016-ms-DatasetNinja"
train_dir = "train"
test_dir = "test"
val_dir = "val"
dirs = (train_dir, test_dir, val_dir)

annotation_dirs_name = 'ann'
annotation_output_dirs_name = 'labels'
images_dirs_name = 'img'
images_output_dirs_name = 'images'

with open(classes_file) as file:
    classes = {value: key for key, value in dict(enumerate(file)).items()}

for directory in dirs:
    directory = Path(dataset_dir) / directory

    old_images_dir = directory / images_dirs_name
    new_images_dir = directory / images_output_dirs_name

    old_annotations_dir = directory / annotation_dirs_name
    new_annotations_dir = directory / annotation_output_dirs_name

    os.rename(old_images_dir, new_images_dir)

    os.mkdir(new_annotations_dir)
    filenames = os.listdir(old_annotations_dir)
    for filename in filenames:
        path = old_annotations_dir / filename
        new_filename = filename.split('.')[0] + '.txt'
        new_path = new_annotations_dir / new_filename
        with open(path) as file_in, open(new_path, 'w') as file_out:
            json_obj = json.load(file_in)
            height, width = json_obj['size'].values()
            objects = json_obj['objects']
            for obj in objects:
                class_id = classes[obj['classTitle']]
                coordinates_1, coordinates_2 = obj['points']['exterior']
                x1, y1 = coordinates_1
                x2, y2 = coordinates_2

                x_center = (x1 + x2) / (2 * width)
                y_center = (y1 + y2) / (2 * height)
                obj_width = (x2 - x1) / width
                obj_height = (y2 - y1) / height

                file_out.write(f"{class_id} {x_center:.6f} {y_center:.6f} {obj_width:.6f} {obj_height:.6f}\n")
    shutil.rmtree(old_annotations_dir)


data = {
    'path': '../' + dataset_dir,
    'train': train_dir,
    'test': test_dir,
    'val': val_dir,
    'names': {value: key for key, value in classes.items()}
}

with open(dataset_name + '.yaml', 'w') as file:
    yaml.dump(data, file)