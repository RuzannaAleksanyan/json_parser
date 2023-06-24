# JSON Parser
The program includes methods for reading JSON data from a file, parsing JSON strings, adding, updating, and deleting fields in JSON objects, and processing user commands to interact with the JSON data.

## Features
- Load JSON file: The load_json_file method allows you to load JSON data from a file and parse it into a Python object.
- Parse JSON string: The parse_json method takes a JSON string as input and parses it into a Python object.
- Add field: The add_field method enables you to add a new field to a JSON object by providing the field expression and the field value.
- Update field: The update_field method allows you to update the value of an existing field in a JSON object by providing the field expression and the new field value.
- Delete field: The delete_field method enables you to delete a field from a JSON object by providing the field expression.
- Process commands: The process_command method allows you to interactively process user commands to add, update, or delete fields in the JSON data.

## Usage
- Run the script by executing the command python3 json_parser.py

## Command Examples
1. Add or update a field:
- student.name = Anna: If there is a student.name field, change its value to "Anna". If not, add the field with the value "Anna".
2. Update a field:
- upd school.name = Academy: Modify the value of the school.name field to "Academy".
3. Delete a field:
- delete student: Delete the student field.
4. Exit the program:
- exit: Terminate the program.

## Random Generation File
The code includes a feature to generate a random JSON file using the generate_json_file() function. 
This function creates a JSON file with random data for the name, age, and address fields.
- To use the random generation feature: python3 random_file_generation.py


## Testing
The JSON Parser code includes a test suite to verify its functionalities..

1. Loading a JSON file and comparing the loaded data with expected data.
2. Parsing a JSON string and comparing the parsed data with expected data.
3. Adding a field to a JSON object and verifying the updated object.
4. Updating a field in a JSON object and verifying the updated value.
5. Deleting a field from a JSON object and verifying its removal.
- To run the test: python json_parser_tests.py

