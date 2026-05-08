import json

def read_json():
    with open(r"test-data\login_data.json",) as file:
        data = json.load(file)
        print(data)
        return data