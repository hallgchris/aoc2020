import os

x_stride = 3
y_stride = 1

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    input_file = os.path.join(script_dir, "input.txt")

    tree_map = []
    with open(input_file) as file:
        tree_map = file.readlines()

    # Subtract one as last char is newline
    width = len(tree_map[0]) - 1
    height = len(tree_map)

    x, y = 0, 0
    tree_count = 0
    while y < height - 1:
        x = (x + x_stride) % width
        y += y_stride
        if tree_map[y][x] == "#":
            tree_count += 1

    print(tree_count)