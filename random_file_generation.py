# import json
import random


def generate_json_file(filename):
    data = {
        'name': random_name(),
        'age': random_age(),
        'address': random_address()
    }

    file = open(filename, 'w')
    file.write(custom_dumps(data))
    print(f"Generated JSON file: {filename}")


def custom_dumps(data, indent=4):
    def dump_dict(d, level=0):
        result = ''
        for key, value in d.items():
            if isinstance(value, dict):
                result += '\t' * level + f'"{key}": ' + dump_dict(value, level + 1) + ',\n'
            else:
                if isinstance(value, str):
                    result += '\t' * level + f'"{key}": "{value}",\n' 
                elif isinstance(value, (int, float)):
                    result += '\t' * level + f'"{key}": {value},\n'
        return '{\n' + result.rstrip(',\n') + '\n' + '\t' * (level - 1) + '}'

    return dump_dict(data, 1)


def random_name():
    names = ['Hayk', 'Nairuhi', 'Davit', 'Nane', 'Njdeh']
    return random.choice(names)


def random_age():
    return random.randint(18, 40)


def random_address():
    streets = ['Monte Melqonyan', 'Levon Shant', 'Sasunci Davit', 'Mesrop Mashtotc']
    cities = ['Martuni', 'Martakert', 'Stepanakert', 'Chartar']

    address = {
        'street': random.choice(streets),
        'city': random.choice(cities),
        'zipcode': random.randint(10000, 99999)
    }

    return address


filename = f'file.json'
generate_json_file(filename)
