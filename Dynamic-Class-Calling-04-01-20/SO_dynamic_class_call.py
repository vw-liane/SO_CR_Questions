from pathlib import Path
import pandas as pd
import inspect

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

def extract_ser():
    sub_cls_ser = {}     # holds the series of grapes -or- cucumbers
    classes_path = Path('Classes')  # starting folder
    for super_class in classes_path.iterdir(): # Path of Fruit -or- Vegetable Folder
        for sub_class in super_class.iterdir(): # Path of <grapes.csv> -or- <cucumbers.csv>
            df_csv = pd.read_csv(sub_class)  # dataframe assignment
            df_ser = df_csv.iloc[:,0]      # series assignment

            sub_cls_ser[eval((sub_class.stem[:-1]).capitalize())] = df_ser  # [ClassName] = series
    return sub_cls_ser


def make_objs(sub_ser):
    for cls_key, ser_val in sub_ser.items():
        make_cls = lambda cls: cls_key()

        print(f"Check DF obj_key: {cls_key} \n Type: {cls_key}")
        obj_df = ser_val.apply(make_cls)        # is safer because only using in .apply()?
        print(f"After .apply()::\nCheck OBJ_DF Contents\n{obj_df}\n")


## RECURSIVE THROUGH TREE
def trav_tree(tree):
    for indx, elem in enumerate(tree):
        for jdx, sub in enumerate(elem):
            print(f"Index: {jdx}\nSub-Elem: {sub}\n\n")


if __name__ == "__main__":
        sub_cls_series = extract_ser()
        make_objs(sub_cls_series)

        cls_list = [Vegetable, Fruit, Grape, Cucumber]
        the_tree = inspect.getclasstree(classes=cls_list)
        trav_tree(the_tree)

        my_fab_cuc = Cucumber()
        print(f"Is my_fab_cuc an instance of Vegetable?: {isinstance(my_fab_cuc, Vegetable)}")
        print(f"Is my_fab_cuc an instance of Cucumber?: {isinstance(my_fab_cuc, Cucumber)}")


