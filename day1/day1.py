import os
from timeit import default_timer
from typing import List

search = 2020

def get_entries(input_file: str):
    script_dir = os.path.dirname(__file__)
    input_file = os.path.join(script_dir, input_file)

    entries = []
    with open(input_file) as file:
        for line in file:
            entries.append(int(line))
    return entries

def part_1(entries: List[int]):
    for i in range(len(entries)):
        for j in range(i + 1, len(entries)):
            if entries[i] + entries[j] == search:
                return entries[i] * entries[j]

    raise Exception(f"Could not find pair summing to {search} :(")

def part_2_bf(entries: List[int]):
    for i in range(len(entries)):
        for j in range(i + 1, len(entries)):
            for k in range(j + 1, len(entries)):
                if entries[i] + entries[j] + entries[k] == search:
                    return entries[i] * entries[j] * entries[k]

    raise Exception(f"Could not find triple summing to {search} :(")

def part_2_sensible(entries: List[int]):
    entries.sort()
    for i in range(len(entries)):
        for j in range(i + 1, len(entries)):
            first, second = entries[i], entries[j]
            if first + second > search:
                continue
            for k in range(j + 1, len(entries)):
                if first + second + entries[k] == search:
                    return first * second * entries[k]

    raise Exception(f"Could not find triple summing to {search} :(")

if __name__ == "__main__":
    entries = get_entries("input.txt")

    start = default_timer()
    print(part_1(entries))
    print(f"Part 1: {default_timer() - start} s")

    start = default_timer()
    print(part_2_bf(entries))
    print(f"Brute force: {default_timer() - start} s")

    start = default_timer()
    entries.sort()
    print(part_2_bf(entries))
    print(f"Brute force with sort: {default_timer() - start} s")

    start = default_timer()
    print(part_2_sensible(entries))
    print(f"Sensible: {default_timer() - start} s")
