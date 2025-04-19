def list_to_dict(lst):
    result = lst[-1]
    for item in reversed(lst[:-1]):
        result = {item: result}
    return result

example = ['2018-01-01', 'yandex', 'cpc', 100]
print(list_to_dict(example))  