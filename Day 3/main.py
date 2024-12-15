"""
Main file for Day 3 AoC.
URL: https://adventofcode.com/2024/day/3
"""
from parser import InputParser


def main():
    """
    Main function for the Day 3 AoC challenge. Init the InputParser.

    Part 1:
        First collects the mul_values from the input file with InputParser. It doesn't check for 'do()' or 'don't()'.
        iterating through the mul values, then multiplying the two numbers together and adding them to a total.

    Part 2:
        It collects the mul parameters from the parser, this time checking for 'do()' and 'don't()'. Then it multiplies
        them, and collects the total.
    """
    parser = InputParser('input.txt')
    mul_values: list[[int, int]] = parser.get_mul_numbers()

    # Part 1
    total_mul: int = 0
    for mul_parameters in mul_values:
        total_mul += mul_parameters[0] * mul_parameters[1]

    print(f"Total Mul: {total_mul}")

    # Entering part 2
    print("\n|\n|\n| PART 2\n|\n|\n")

    do_check_values: list[[int, int]] = parser.get_do_check_mul_numbers()

    total_do_checked_values: int = 0
    for mul_parameters in do_check_values:
        total_do_checked_values += mul_parameters[0] * mul_parameters[1]

    print(f"Total Do Checked Mul: {total_do_checked_values}")


if __name__ == '__main__':
    main()
