import os
import numpy as np

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    input_file = os.path.join(script_dir, "input.txt")

    yes_answer_count = 0
    all_yes_answer_count = 0
    with open(input_file) as file:
        current_yeses = [0] * 26
        current_people_in_group = 0
        for line in file:
            line = line.strip()
            if not line:
                yes_answer_count += np.count_nonzero(current_yeses)
                all_yes_answer_count += current_yeses.count(current_people_in_group)
                current_yeses = [0] * 26
                current_people_in_group = 0
            else:
                current_people_in_group += 1
                for char in line:
                    current_yeses[ord(char) - ord("a")] += 1
    yes_answer_count += np.count_nonzero(current_yeses)
    all_yes_answer_count += current_yeses.count(current_people_in_group)
    print(yes_answer_count, "questions answered 'yes'")
    print(all_yes_answer_count, "questions where everyone answered 'yes'")
