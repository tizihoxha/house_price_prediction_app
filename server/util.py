import json
import pickle
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# Global variables
__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bedrooms, bathrooms):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = bedrooms
    x[1] = bathrooms
    x[2] = sqft
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

def load_saved_artifacts():
    print("loading")
    global __data_columns
    global __locations

    with open("C:\\Users\\CRS\\Desktop\\House_price_prediction\\House_price_prediction\\server\\artifacts\\columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    if __model is None:
        with open("C:\\Users\\CRS\\Desktop\\House_price_prediction\\House_price_prediction\\server\\artifacts\\home_price_prediction.pickle", 'rb') as f:
            __model = pickle.load(f)

    print("loading done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('Vancouver', 1200, 1, 3))
    print(get_estimated_price('Vancouver', 1265, 2, 3))
    print(get_estimated_price('San Jose', 1200, 2, 2))
    print(get_estimated_price('Staten Island', 967, 1, 2))
