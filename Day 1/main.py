"""
URL: https://adventofcode.com/2024/day/1
"""
from connection import IDConnection
from parser import InputParser


def main() -> None:
    """
    Gets both parsed lists, then sorts both lists (smallest to biggest)

    Part 1:
        Goes through left & right lists, and then adds the connected points to an id connections list to easily
        print out and control the data in a custom class.

    Part 2:
        Iterate through the left list, and multiply it by the amount of times that number appears in the right list,
        then adds that to a total number.
    """
    left_location_ids, right_location_ids = InputParser("input.txt").get_parsed_input()

    left_location_ids.sort()
    right_location_ids.sort()

    # Part 1
    id_connections: list[IDConnection] = []
    for i in range(len(left_location_ids)):
        id_connections.append(IDConnection(left_location_ids[i], right_location_ids[i]))

    for i, connection in enumerate(id_connections):
        print(f"{i + 1}: Left ID: {connection.id_1}  Right ID: {connection.id_2}"
              f" | Total Distance: {connection.difference}")
    print(f"Total Distance between location IDs: {sum(map(lambda c: c.difference, id_connections))}")

    # Entering part 2
    print("\n|\n|\n| PART 2\n|\n|\n")

    total: int = 0
    for i in range(len(left_location_ids)):
        # Number of left list * amount of times number appears in right list
        result: int = left_location_ids[i] * right_location_ids.count(left_location_ids[i])
        total += result
        print(f"{i + 1}: {left_location_ids[i]} * {right_location_ids.count(left_location_ids[i])} = {result}")

    print(f"Total similarity score: {total}")


# Running Main Function for AoC day 1.
if __name__ == '__main__':
    main()
