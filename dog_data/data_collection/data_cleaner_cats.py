import os
import json
import requests
from dog_data.data_collection import column_filler


# pulls data from the dog api to create a cleaned list of data which encapsulates dictionaries by breed
# also cleans the data with nested methods
def request_and_clean_data() -> list:
    base_url = 'https://api.thecatapi.com/'
    breeds_endpoint = "v1/breeds"
    api_key = '?api_key=live_a3GdV3X1EneWyzP1gM5phCvGM9o8giQNY3gpzHrWoryAzbjBe1B4iRC88KAqMMtK'
    column_attributes = ['weight', 'id', 'name', 'cfa_url', 'vetstreet_url', 'vcahospitals_url',
                         'temperament', 'origin', 'country_codes', 'country_code', 'description',
                         'life_span', 'indoor', 'lap', 'alt_names', 'adaptability', 'affection_level',
                         'child_friendly', 'cat_friendly', 'dog_friendly', 'energy_level', 'grooming',
                         'health_issues', 'intelligence', 'shedding_level', 'social_needs',
                         'stranger_friendly', 'vocalisation', 'bidability', 'experimental', 'hairless',
                         'natural', 'rare', 'rex', 'suppressed_tail', 'short_legs', 'wikipedia_url',
                         'hypoallergenic', 'reference_image_id']
    breeds_request_str = base_url + breeds_endpoint + api_key
    response = requests.get(breeds_request_str).json()
    response_to_list = list(response)
    return clean_data(response_to_list, column_attributes)


# separate API call to receive image links to display on the view
def request_picture(name):
    base_url = 'https://api.thecatapi.com/'
    image_endpoint = "v1/images/" + name + '/'
    api_key = os.environ.get('API_KEY')
    image_request_str = base_url + image_endpoint + api_key
    response = requests.get(image_request_str).json()
    response_to_list = dict(response)
    return response_to_list['url']


# adds column attributes that are missing from the data
def clean_data(response_to_list: list, column_attributes: list) -> list:
    for i in range(len(column_attributes) - 1):
        response_to_list = column_filler.add_NA_item_to_dict(response_to_list, column_attributes[i + 1],
                                                             column_attributes[i])
    return response_to_list


# deletes unwanted columns from every cat model to be
def del_unwanted_data(cleaned_list):
    for item in cleaned_list:
        del item['id']
        del item['alt_names']
        del item['cat_friendly']
        del item['energy_level']
        del item['stranger_friendly']
        del item['bidability']
        del item['rex']
        del item['suppressed_tail']
    return cleaned_list


# takes inputs, the index prior to the value needed to be added to the data, and the key name
# fills out every missing key value pair for a key with value of N/A
def add_view_data():
    data = del_unwanted_data(request_and_clean_data())
    final_json = []
    for item in data:
        left_values = [i for i in range(0, 121, 30)]
        item.update({'left': left_values})

        if not item['reference_image_id'] == 'N/A':
            image_id = item['reference_image_id']
            image_url = request_picture(image_id)
        else:
            image_url = 'https://react.semantic-ui.com/images/wireframe/image.png'
        item.update({'image_url': image_url})

        items_list = []
        values_list = []
        column_attributes = ['indoor', 'lap', 'adaptability', 'affection_level', 'child_friendly',
                             'dog_friendly', 'grooming', 'health_issues', 'intelligence', 'shedding_level',
                             'social_needs', 'vocalisation', 'experimental', 'hairless', 'natural',
                             'rare', 'short_legs', 'hypoallergenic']

        for key in column_attributes:
            if item[key] != 'N/A' and item[key] != 0 and item[key] != '':
                items_list.append(key)

        if 'indoor' in items_list:
            values_list.append(("Indoor Prone:", item['indoor']))
        del item['indoor']
        if 'lap' in items_list:
            values_list.append(("Lap Friendly:", item['lap']))
        del item['lap']
        if 'adaptability' in items_list:
            values_list.append(("Adaptability:", item['adaptability']))
        del item['adaptability']
        if 'affection_level' in items_list:
            values_list.append(("Affection:", item['affection_level']))
        del item['affection_level']
        if 'child_friendly' in items_list:
            values_list.append(("Child Friendly:", item['child_friendly']))
        del item['child_friendly']
        if 'dog_friendly' in items_list:
            values_list.append(("Dog Friendly:", item['dog_friendly']))
        del item['dog_friendly']
        if 'grooming' in items_list:
            values_list.append(("Grooming Frequency:", item['grooming']))
        del item['grooming']
        if 'health_issues' in items_list:
            values_list.append(("Health:", item['health_issues']))
        del item['health_issues']
        if 'intelligence' in items_list:
            values_list.append(("Intellect:", item['intelligence']))
        del item['intelligence']
        if 'shedding_level' in items_list:
            values_list.append(("Shedding Level:", item['shedding_level']))
        del item['shedding_level']
        if 'social_needs' in items_list:
            values_list.append(("Social Needs:", item['social_needs']))
        del item['social_needs']
        if 'vocalisation' in items_list:
            values_list.append(("Vocalization:", item['vocalisation']))
        del item['vocalisation']
        if 'experimental' in items_list:
            values_list.append(("Playfulness:", item['experimental']))
        del item['experimental']
        if 'hairless' in items_list:
            values_list.append(("Hairless:", item['hairless']))
        del item['hairless']
        if 'natural' in items_list:
            values_list.append(("Natural:", item['natural']))
        del item['natural']
        if 'rare' in items_list:
            values_list.append(("Rarity:", item['rare']))
        del item['rare']
        if 'short_legs' in items_list:
            values_list.append(("Short Legs:", item['short_legs']))
        del item['short_legs']
        if 'hypoallergenic' in items_list:
            values_list.append(("Hypoallergenic:", item['hypoallergenic']))
        del item['hypoallergenic']
        item.update({"stars": values_list})
        final_json.append(item)
    return final_json


# prints all the data, from call to clean as a JSON to be interpreted by the command and injected into the db
def print_clean_data_to_file():
    clean_response = add_view_data()
    clean_response_json = json.dumps(clean_response)
    file_out = open('../../clean_json_cats.txt', 'w')
    print(clean_response_json, file=file_out)
    file_out.close()


# main for testing
def main():
    print_clean_data_to_file()


if __name__ == '__main__':
    main()
