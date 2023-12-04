import os
import json
import requests
from dog_data.data_collection import column_filler


# pulls data from the dog api to create a cleaned list of data which encapsulates dictionaries by breed
# also cleans the data with nested methods
def data_request():
    base_url = 'https://api.thedogapi.com/'
    breeds_endpoint = "v1/breeds"
    api_key = os.environ.get('API_KEY')
    column_attributes = ['weight', 'height', 'id', 'name', 'description', 'country_code', 'bred_for', 'breed_group',
                         'life_span', 'history', 'temperament', 'origin', 'reference_image_id', 'image']
    breeds_request_str = base_url + breeds_endpoint + api_key
    response = requests.get(breeds_request_str).json()
    response_to_list = list(response)
    return clean_data(response_to_list, column_attributes)


# deletes unwanted columns from every cat model to be
def del_unwanted_data(cleaned_list):
    for item in cleaned_list:
        del item['id']
    return cleaned_list


# adds column attributes that are missing from the data
def clean_data(response_to_list: list, column_attributes: list) -> list:
    # every breed has a respective image, no need to add N/A for the image url as it is always full
    for i in range(len(column_attributes)):
        response_to_list = column_filler.add_NA_item_to_dict(response_to_list, column_attributes[i], column_attributes[i - 1])
    return response_to_list


# prints all the data, from call to clean as a JSON to be interpreted by the command and injected into the db
def print_clean_data_to_file():
    clean_response = del_unwanted_data(data_request())
    clean_response_json = json.dumps(clean_response)
    file_out = open('../../clean_json_dogs.txt', 'w')
    print(clean_response_json, file=file_out)
    file_out.close()


# main for testing
def main():
    print_clean_data_to_file()


if __name__ == '__main__':
    main()
