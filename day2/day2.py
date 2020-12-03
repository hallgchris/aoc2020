import os
import re

def verify_password(min_count: int, max_count: int, policy_char: str, password: str):
    counter = 0
    for char in password:
        if char == policy_char:
            counter += 1
    return min_count <= counter <= max_count

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    input_file = os.path.join(script_dir, "input.txt")

    pattern = re.compile(r"(?P<min>\d+)-(?P<max>\d+) (?P<char>[a-z]): (?P<password>[a-z]*)")

    valid = 0

    with open(input_file) as file:
        for line in file:
            match = pattern.match(line)
            min_count = int(match.group("min"))
            max_count = int(match.group("max"))
            char = match.group("char")
            password = match.group("password")
            if verify_password(min_count, max_count, char, password):
                valid += 1

    print(f"{valid} valid passwords")
