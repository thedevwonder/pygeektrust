from sys import argv

power_per_turn = 5
power_per_move = 10


def main():
    sX = 0
    sY = 0
    dX = 0
    dY = 0
    dir = ""

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, "r")
    lines = f.readlines()

    for line in lines:
        tokens = line.split()
        if tokens[0] == "SOURCE":
            sX = int(tokens[1])
            sY = int(tokens[2])
            dir = tokens[3]

        if tokens[0] == "DESTINATION":
            dX = int(tokens[1])
            dY = int(tokens[2])

        if tokens[0] == "PRINT_POWER":
            p = calculate_power(sX, sY, dX, dY, dir)
            print("POWER %3d" % (p))


def calculate_power(sX, sY, dX, dY, dir):
    relative_dx = dX - sX
    relative_dy = dY - sY

    power_spent = calculate_power_spent(relative_dx, relative_dy, dir)
    return 200 - power_spent


def calculate_power_spent(relative_dx, relative_dy, dir):
    power_spent = 0

    if relative_dx > 0 and relative_dy > 0:
        power_spent += remaining_power_first_quad(relative_dx, relative_dy, dir)
    elif relative_dx < 0 and relative_dy > 0:
        power_spent += remaining_power_second_quad(relative_dx, relative_dy, dir)

    elif relative_dx < 0 and relative_dy < 0:
        power_spent += remaining_power_third_quad(relative_dx, relative_dy, dir)

    elif relative_dx > 0 and relative_dy < 0:
        power_spent += remaining_power_fourth_quad(relative_dx, relative_dy, dir)

    elif relative_dx == 0 and relative_dy > 0:
        power_spent += remaining_power_pos_y(relative_dy, dir)

    elif relative_dx == 0 and relative_dy < 0:
        power_spent += remaining_power_neg_y(relative_dy, dir)

    elif relative_dy == 0 and relative_dx < 0:
        power_spent += remaining_power_neg_x(relative_dx, dir)

    elif relative_dy == 0 and relative_dx > 0:
        power_spent += remaining_power_pos_x(relative_dx, dir)

    elif relative_dx == 0 and relative_dy == 0:
        power_spent += 0

    return power_spent


def remaining_power_first_quad(relative_dx, relative_dy, dir):
    total_moves = 0
    turns = 0
    if dir == "N" or dir == "E":
        turns += power_per_turn
        total_moves = power_per_move * (abs(relative_dx) + abs(relative_dy))
    if dir == "S" or dir == "W":
        turns += 2 * power_per_turn
        total_moves = power_per_move * (abs(relative_dx) + abs(relative_dy))
    return turns + total_moves


def remaining_power_second_quad(relative_dx, relative_dy, dir):
    total_moves = 0
    turns = 0
    if dir == "N" or dir == "W":
        turns += power_per_turn
        total_moves = power_per_move * (abs(relative_dx) + abs(relative_dy))
    if dir == "S" or dir == "E":
        turns += 2 * power_per_turn
        total_moves = power_per_move * (abs(relative_dx) + abs(relative_dy))
    return turns + total_moves


def remaining_power_third_quad(relative_dx, relative_dy, dir):
    total_moves = 0
    turns = 0
    if dir == "N" or dir == "E":
        turns += 2 * power_per_turn
        total_moves = power_per_move * (abs(relative_dx) + abs(relative_dy))
    if dir == "S" or dir == "W":
        turns += power_per_turn
        total_moves = power_per_move * (abs(relative_dx) + abs(relative_dy))
    return turns + total_moves


def remaining_power_fourth_quad(relative_dx, relative_dy, dir):
    total_moves = 0
    turns = 0
    if dir == "N" or dir == "W":
        turns += 2 * power_per_turn
        total_moves = power_per_move * (abs(relative_dx) + abs(relative_dy))
    if dir == "S" or dir == "E":
        turns += power_per_turn
        total_moves = power_per_move * (abs(relative_dx) + abs(relative_dy))
    return total_moves + turns


def remaining_power_pos_y(relative_dy, dir):
    total_moves = 0
    turns = 0
    if dir == "N":
        turns += 0
        total_moves = power_per_move * abs(relative_dy)
    if dir == "E" or dir == "W":
        turns += power_per_turn
        total_moves = power_per_move * abs(relative_dy)
    if dir == "S":
        turns += 2 * power_per_turn
        total_moves = power_per_move * abs(relative_dy)
    return total_moves + turns


def remaining_power_neg_y(relative_dy, dir):
    total_moves = 0
    turns = 0
    if dir == "S":
        turns += 0
        total_moves = power_per_move * abs(relative_dy)
    if dir == "E" or dir == "W":
        turns += power_per_turn
        total_moves = power_per_move * abs(relative_dy)
    if dir == "N":
        turns += 2 * power_per_turn
        total_moves = power_per_move * abs(relative_dy)
    return total_moves + turns


def remaining_power_neg_x(relative_dx, dir):
    total_moves = 0
    turns = 0
    if dir == "W":
        turns += 0
        total_moves = power_per_move * abs(relative_dx)
    if dir == "N" or dir == "S":
        turns += power_per_turn
        total_moves = power_per_move * abs(relative_dx)
    if dir == "E":
        turns += 2 * power_per_turn
        total_moves = power_per_move * abs(relative_dx)
    return total_moves + turns


def remaining_power_pos_x(relative_dx, dir):
    total_moves = 0
    turns = 0
    if dir == "E":
        turns += 0
        total_moves = power_per_move * abs(relative_dx)
    if dir == "N" or dir == "S":
        turns += power_per_turn
        total_moves = power_per_move * abs(relative_dx)
    if dir == "W":
        turns += 2 * power_per_turn
        total_moves = power_per_move * abs(relative_dx)
    return total_moves + turns


if __name__ == "__main__":
    main()
