import json
import pickle

__locations  = None
__data_columns = None
__model = None

def get_location_names():
    return __locations

def load_saved_data():
    print("loading saved data")
    global __data_columns
    global __locations
    
    with open("C:\\Users\\User\\Desktop\\house_price_prediction_app\\server\\artifacts\\columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]
    
    with open("C:\\Users\\User\\Desktop\\house_price_prediction_app\\server\\artifacts\\house_price_prediction.pickle", "rb") as f:
        __model = pickle.load(f)
    print("Losding data has finished!")
    
if __name__ == '__main__':
    load_saved_data()    
    print(get_location_names())