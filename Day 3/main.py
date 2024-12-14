"""
Main file for Day 3 AoC.
URL: https://adventofcode.com/2024/day/3
"""
from parser import InputParser


def main():
    """
    Main function for the Day 3 AoC challenge. First collects the mul_values from the input file with InputParser.
    """
    mul_values: list[set[int, int]] = InputParser("input.txt").get_mul_numbers()


if __name__ == '__main__':
    main()
