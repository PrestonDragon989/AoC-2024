"""
File to house the input parser for Day 2.
Input URL: https://adventofcode.com/2024/day/2/input
"""


class InputParser:
    def __init__(self, file_path: str) -> None:
        self._file_path: str = file_path

    def get_parsed_lists(self) -> list[list[int]]:
        """
        Gets the parsed data from the given file path.
        @return: A list of lists, comprised of integers
        """
        parsed_lists: list[list[int]] = []

        with open(self._file_path, "r") as f:
            for line in f.readlines():
                parsed_lists.append(list(map(lambda n: int(n), line.split(" "))))

        return parsed_lists
