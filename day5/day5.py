import os

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    input_file = os.path.join(script_dir, "input.txt")

    maximum_seat_id = 0
    filled_seats = [False] * 128 * 8
    with open(input_file) as file:
        for line in file:
            next_row_value = 64
            next_col_value = 4
            row_id = 0
            col_id = 0
            for char in line.strip():
                if char in ["F", "B"]:
                    if char == "B":
                        row_id += next_row_value
                    next_row_value //= 2
                elif char in ["L", "R"]:
                    if char == "R":
                        col_id += next_col_value
                    next_col_value //= 2
            seat_id = row_id * 8 + col_id
            filled_seats[seat_id] = True
            maximum_seat_id = max(maximum_seat_id, seat_id)
    print("Maximum seat ID:", maximum_seat_id)

    for i in range(1, 128*8 - 1):
        if filled_seats[i-1] and not filled_seats[i] and filled_seats[i+1]:
            print("My seat:", i)