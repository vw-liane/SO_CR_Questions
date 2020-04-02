from pathlib import Path
import pandas as pd

## SUPER CLASSES
################
class Fruit(object):
    def __init__(self):
        self.name = "fruit"

    def __str__(self):
        return f"{self.name} object"

class Vegetable(object):
    def __init__(self):
        self.name = "vegetable"

    def __str__(self):
        return f"{self.name} object"

## SUB CLASSES
##############
class Grape(Fruit):
    def __init__(self):
        self.name = "grape"

    def __str__(self):
        return f"{self.name} object"

class Cucumber(Vegetable):
    def __init__(self):
        self.name = "cucumber"

    def __str__(self):
        return f"{self.name} object"

def extract_abbv():
    df_abvs = {}     # holds the DFs of abvs of individual grapes -or- cucumbers
    classes_path = Path('Classes')  # starting folder
    for super_class in classes_path.iterdir(): # Path of Fruit -or- Vegetable Folder
        for sub_class in super_class.iterdir(): # Path of <grapes.csv> -or- <cucumbers.csv>
            f_name_str = str(sub_class.name)

    return classes_path, df_abvs

def make_objs(cls_fldr_pth):


    for super_class in cls_fldr_pth.iterdir():
        for sub_class in super_class.iterdir():
            # how can I call here the coorresponding SUB & SUPER
            # class constructors?
            print(f"File Stem: {sub_class.stem}")  # no errors when test running


make_objs()