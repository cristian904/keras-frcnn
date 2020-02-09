import io
import json
import os
import shutil
import random

DATASET_DIR = "../data/"
TRAIN_IMAGES_DIR = "./train_images/"

def copy_image(image_name, from_folder, to_folder):
    os.rename(from_folder + image_name, to_folder + image_name)
    return to_folder + image_name

def parse_json(path):
    with io.open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    f = io.open("annotation_lines.txt", "w", encoding="utf-8")

    annotations = data[2]["data"]
    for annotation in annotations:
        if annotation["annotation_type"] == "line" and annotation["annotation_value"] != ",":
            if os.path.exists(DATASET_DIR + annotation["set_no"] + "/images/" + annotation["image_name"]):
                new_path = TRAIN_IMAGES_DIR + annotation["set_no"] + "_" + annotation["image_name"]
                shutil.copy(DATASET_DIR + annotation["set_no"] + "/images/" + annotation["image_name"], new_path)
                f.write(new_path + "," + annotation['x_min'] + "," + annotation["y_min"] + "," + annotation['x_max'] + "," + annotation["y_max"] + "," + annotation["annotation_type"] + "\n")



parse_json("annotations.json")
