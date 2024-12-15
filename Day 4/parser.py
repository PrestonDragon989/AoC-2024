"""
The file that houses the class InputParser.
Input URL: https://adventofcode.com/2024/day/4/input
"""


class InputParser:
    def __init__(self, file_name: str) -> None:
        self._file_name = file_name

    def get_word_search_lines(self) -> list[str]:
        """
        @return: The lines in the word search input. (the given file)
        """
        with open(self._file_name, "r") as f:
            return f.readlines()
