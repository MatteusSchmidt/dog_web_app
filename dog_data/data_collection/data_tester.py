# returns a value with its corresponding name
def get_column_data(clean_response, name, request) -> str:
    for item in clean_response:
        if item['name'] == name:
            return item[request]
