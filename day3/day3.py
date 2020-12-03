import os

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    input_file = os.path.join(script_dir, "input.txt")

    tree_map = []
    with open(input_file) as file:
        tree_map = file.readlines()

    # Subtract one as last char is newline
    width = len(tree_map[0]) - 1
    height = len(tree_map)

    tree_product = 1

    for slope in slopes:
        x, y = 0, 0
        tree_count = 0
        while y < height - 1:
            x = (x + slope[0]) % width
            y += slope[1]
            if tree_map[y][x] == "#":
                tree_count += 1
        tree_product *= tree_count

    print(tree_product)