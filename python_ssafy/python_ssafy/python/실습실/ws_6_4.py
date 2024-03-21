# 아래 함수를 수정하시오.
def get_keys_from_dict(dict_):
    return list(dict_.keys())


my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']
