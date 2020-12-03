import os
import re

def verify_password_part_1(min_count: int, max_count: int, policy_char: str, password: str):
    counter = 0
    for char in password:
        if char == policy_char:
            counter += 1
    return min_count <= counter <= max_count

def verify_password_part_2(first_index: int, second_index: int, policy_char: str, password: str):
    first_result = first_index - 1 < len(password) and password[first_index - 1] == char
    second_result = second_index - 1 < len(password) and password[second_index - 1] == char
    return first_result ^ second_result

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    input_file = os.path.join(script_dir, "input.txt")

    pattern = re.compile(r"(?P<min>\d+)-(?P<max>\d+) (?P<char>[a-z]): (?P<password>[a-z]*)")

    valid_part_1, valid_part_2 = 0, 0

    with open(input_file) as file:
        for line in file:
            match = pattern.match(line)
            min_count = int(match.group("min"))
            max_count = int(match.group("max"))
            char = match.group("char")
            password = match.group("password")
            if verify_password_part_1(min_count, max_count, char, password):
                valid_part_1 += 1
            if verify_password_part_2(min_count, max_count, char, password):
                valid_part_2 += 1

    print(f"{valid_part_1} valid passwords (part 1 policy)")
    print(f"{valid_part_2} valid passwords (part 2 policy)")
