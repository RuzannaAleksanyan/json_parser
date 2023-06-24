from json_parser import JSONParser

def test_load_json_file():
    parser = JSONParser()

    test_data = {'name': 'John', 'age': 30}
    file_path = 'test.json'

    with open(file_path, 'w') as file:
        file.write(parser.custom_dumps(test_data))

    data = parser.load_json_file(file_path)

    if data == test_data:
        print("JSON file load test passed!")
    

def test_parse_json():
    json_str = '''
        {
            "name": "Roz",
            "age": 30,
            "address": {
                "street": "Monte Melqonyan",
                "city": "Chartar",
                "zipcode": 45566
            }
        }
    '''

    expected_data = {
        "name": "Roz",
        "age": 30,
        "address": {
            "street": "Monte Melqonyan",
            "city": "Chartar",
            "zipcode": 45566
        }
    }

    parser = JSONParser()
    data = parser.parse_json(json_str)
    if data == expected_data:
        print("JSON parsing test passed!")


def test_add_field():
    data = {}
    field_expr = 'person.name'
    field_value = 'John'

    parser = JSONParser()
    parser.add_field(data, field_expr, field_value)

    if data['person']['name'] == 'John':
        print("JSON add field test passed!")


def test_update_field():
    data = {'person': {'name': 'John', 'age': 30}}
    field_expr = 'person.age'
    field_value = 35
    parser = JSONParser()
    parser.update_field(data, field_expr, field_value)

    if data['person']['age'] == 35:
        print("JSON update field test passed!")


def test_delete_field():
    data = {'person': {'name': 'John', 'age': 30}}
    field_expr = 'person.age'
    parser = JSONParser()
    parser.delete_field(data, field_expr)

    if 'age' not in data['person']:
        print("JSON delete field test passed!")


def run_tests():
    test_load_json_file()
    test_parse_json()
    test_add_field()
    test_update_field()
    test_delete_field()


if __name__ == '__main__':
    run_tests()
