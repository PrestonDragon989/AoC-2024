"""
Main file for Day 3 AoC.
URL: https://adventofcode.com/2024/day/3
"""
from parser import InputParser


def main():
    """
    Main function for the Day 3 AoC challenge. First collects the mul_values from the input file with InputParser.

    Part 1:
        iterating through the mul values, then multiplying the two numbers together and adding them to a total.
    """
    mul_values: list[[int, int]] = InputParser("input.txt").get_mul_numbers()

    print(mul_values)
    print(len(mul_values))

    # Part 1
    total_mul: float = 0
    for mul_parameters in mul_values:
        total_mul += mul_parameters[0] * mul_parameters[1]

    print(f"Total Mul: {total_mul}")


if __name__ == '__main__':
    main()
