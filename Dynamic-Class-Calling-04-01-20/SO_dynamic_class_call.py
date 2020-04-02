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

def extract_ser():
    sub_cls_ser = {}     # holds the series of grapes -or- cucumbers
    classes_path = Path('Classes')  # starting folder
    for super_class in classes_path.iterdir(): # Path of Fruit -or- Vegetable Folder
        for sub_class in super_class.iterdir(): # Path of <grapes.csv> -or- <cucumbers.csv>
            df_csv = pd.read_csv(sub_class)  # dataframe assignment
            df_ser = df_csv.iloc[:, 0]      # series assignment

            sub_cls_ser[sub_class.stem] = df_ser  # [stem] = series
    return classes_path, sub_cls_ser


def make_objs(cls_fldr_pth, sub_ser):
    for super_class in cls_fldr_pth.iterdir():
        make_veg = lambda veg: Vegetable()  # INSERT varying named lambda function & CONSTRUCTOR CALL
                                            #  later applied to series
        ## APPLY super_constr
        for str_key, ser_val in sub_ser.items():
            print(f"Check DF str_key: {str_key}")  # use <str_key> to check which is super class
            obj_df = ser_val.apply(make_veg)     # inside .apply() would change based on super_class

            print(f"After SUPER .apply()::\nCheck OBJ_DF Contents\n{obj_df}\n")

        for sub_class in super_class.iterdir():
            sub_constr = sub_class.stem      # based on this call subclass constructor

            make_cuc = lambda veg: Cucumber()  # INSERT varying named lambda function & CONSTRUCTOR CALL
                                                #  later applied to the series
            for str_key, df_val in sub_ser.items():
                ## APPLY sub_constr
                print(f"Check DF str_key: {str_key}")
                obj_df = df_val.apply(make_cuc)    # inside .apply() would change based on sub_class

                print(f"After SUB .apply()::\nCheck OBJ_DF Contents\n{obj_df}\n")

if __name__ == "__main__":
        classes_flder_path, sub_cls_series = extract_ser()
        make_objs(classes_flder_path, sub_cls_series)
        
        
        
## WHAT I HAVE TRIED
## to write at the beginning of make_objs()
###################

# make lambda function
#lam_func = "make_" + (str(sub_class.stem))[:3]   # first 3 char
#cls_call = (str(sub_class.stem)).capitalize()
#lam_func = lambda fst_3_char: cls_call()       # error string not callable

# Is there a way to call the Class constructor
# by checking if something matches the class name?
# .... for example, if <cls_call> matches the name?
