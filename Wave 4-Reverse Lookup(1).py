def reverse(dictionary, lookup_value):
    list = [key for key, value in dictionary.items() if value == lookup_value]
    return list
