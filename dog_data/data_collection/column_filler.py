def add_NA_item_to_dict(response: list, key_str: str, index_value: str) -> list:
    return_list = []
    dictionary_input = {key_str: 'N/A'}
    for item in response:
        if key_str not in item:
            dictionary_return = {}
            for i in item:
                if not i == index_value:
                    dictionary_return.update({i: item[i]})
                else:
                    dictionary_return.update({index_value: item[index_value]})
                    dictionary_return.update(dictionary_input)
            return_list.append(dictionary_return)
        else:
            return_list.append(item)

    return return_list
