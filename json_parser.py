class JSONParser:
    def __init__(self):
        self.index = 0

    def load_json_file(self, file_path):
        with open(file_path, "r") as file:
            file_contents = file.read()
        return self.parse_json(file_contents)

    

    def parse_json(self, json_str):
        json_str = json_str.replace(" ", "")
        json_str = json_str.replace("\n", "")
        json_str = json_str.replace('\t', '')

        if json_str[0] == "{" and json_str[-1] == "}":
            return self.parse_value(json_str)
        else:
            print("invalid JSON file")
            return


    def parse_value(self, json_str):
        if json_str[self.index] == "{":
            return self.parse_object(json_str)
        elif json_str[self.index] == '"':
            return self.parse_string(json_str)
        else:
            return self.parse_int(json_str)


    def parse_int(self, json_str):
        start = self.index

        if json_str[self.index] == "-":
            self.index += 1

        while self.index < len(json_str) and json_str[self.index].isdigit():
            self.index += 1

        num_str = json_str[start:self.index]

        return int(num_str)


    def parse_string(self, json_str):
        self.index += 1
        start = self.index

        while self.index < len(json_str):
            if json_str[self.index] == '"':
                self.index += 1
                return json_str[start : self.index - 1]
            else:
                self.index+=1

        raise SyntaxError("Invalid JSON string")


    def parse_object(self, json_str):
        self.index += 1
        result = {}

        if json_str[self.index] == "}":
            self.index += 1
            return result

        while 1:
            key = self.parse_string(json_str)

            if json_str[self.index] != ":":
                print("invalid JSON file")
                return
            self.index += 1

            value = self.parse_value(json_str)
            result[key] = value

            if json_str[self.index] == ",":
                self.index += 1
            elif json_str[self.index] == "}":
                self.index += 1
                return result
            else:
                raise SyntaxError("Invalid JSON file")

        return result

    def custom_dumps(self, data, indent=4):
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


    def add_field(self, data, field_expr, field_value):
        fields = field_expr.split('.')
        cur_data = data
        for i in range(len(fields) - 1):
            if fields[i] not in cur_data:
                cur_data[fields[i]] = {}
            cur_data = cur_data[fields[i]]

        if field_value.isdigit():
            cur_data[fields[-1]] = int(field_value)
        else:
            cur_data[fields[-1]] = field_value


    def update_field(self, data, field_expr, field_value):
        field = field_expr.split('.')
        if type(field) != list:
            print("Invalid command. Please provide a valid field name and value.")
            return
        for i in range(len(field) - 1):
            data = data[field[i]]

        data[field[-1]] = field_value


    def delete_field(self, data, field_expr):
        field = field_expr.split('.')
        if len(field) < 1:
            print("Invalid command. Please provide a valid field name.")
            return

        cur_data = data
        for i in field[:-1]:
            if i in cur_data:
                cur_data = cur_data[i]
            else:
                print(f"Nested field '{i}' does not exist.")
                return

        if field[-1] in cur_data:
            del cur_data[field[-1]]
        else:
            print(f"Field '{field_expr}' does not exist.")


    def process_command(self, data, command):
        command = command.strip()  

        if command.startswith('upd'):
            parts = command[3:].strip().split('=')
            if len(parts) != 2:
                print("Invalid command. Please provide a valid field name and value.")
                return

            field_expr = parts[0].strip()
            field_value = parts[1].strip()
            self.update_field(data, field_expr, field_value)

        elif command.startswith('del'):
            field_expr = command[3:].strip()
            if not field_expr:
                print("Invalid command. Please provide a valid field name.")
                return

            self.delete_field(data, field_expr)

        else:
            parts = command.split('=')
            if len(parts) != 2:
                print("Invalid command. Please provide a valid command.")
                return

            field_expr = parts[0].strip()
            field_value = parts[1].strip()

            self.add_field(data, field_expr, field_value)
        with open('file.json', 'w') as file:
            file.write(self.custom_dumps(data))


def main():
    path = 'file.json'
    obj = JSONParser()
    data = obj.load_json_file(path)

    print(obj.custom_dumps(data))

    while True:
        print("Enter a command")
        print("'student.name = Anna' - if there is a student.name member, then change the value, if not, add it")
        print("'upd school.name = Academy' - modify the value of the member school.name")
        print("'delete student' - delete student member")
        print("'exit' - exit the program")
        command = input()
        if command == 'exit':
            break

        obj.process_command(data, command)

    print("Program terminated.")


if __name__ == "__main__":
    main()
