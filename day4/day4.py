from collections import defaultdict
import os
from string import hexdigits

def is_field_valid(field: str, value: str):
    if field == "byr":
        return 1920 <= int(value) <= 2002
    elif field == "iyr":
        return 2010 <= int(value) <= 2020
    elif field == "eyr":
        return 2020 <= int(value) <= 2030
    elif field == "hgt":
        height, unit = value[:-2], value[-2:]
        if height: height = int(height)
        return (unit == "cm" and 150 <= height <= 193) or (unit == "in" and 59 <= height <= 76)
    elif field == "hcl":
        return value[0] == "#" and all(c in hexdigits for c in value[1:])
    elif field == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif field == "pid":
        return len(value) == 9 and value.isdigit()
    elif field == "cid":
        return True
    else:
        return False

class Passport:
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    def __init__(self):
        self.fields = defaultdict(str)

    def __setitem__(self, key: str, value: str):
        if is_field_valid(key, value):
            self.fields[key] = value

    def is_valid(self):
        for field in Passport.required_fields:
            if field not in self.fields:
                return False
        return True

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    input_file = os.path.join(script_dir, "input.txt")

    valid_passports = 0
    with open(input_file) as file:
        current_passport = Passport()
        for line in file:
            line = line.strip()
            if not line:
                if current_passport.is_valid():
                    valid_passports += 1
                current_passport = Passport()
            else:
                fields = line.split(" ")
                for field in fields:
                    [key, value] = field.split(":")
                    current_passport[key] = value

    if current_passport.is_valid():
        valid_passports += 1
        
    print(f"Valid passports: {valid_passports}")
