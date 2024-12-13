"""
This the file for the input parser. This houses the class InputParser, to then return the two lists of parsed input.
"""


class InputParser:
    def __init__(self, file_path: str) -> None:
        self._file_path = file_path

    def get_parsed_input(self) -> tuple[list, list]:
        """
        Goes through the input file, line by line and gets the integers. It then adds them to 2 lists, then returns
        those parsed lists.
        :return: Return the two parsed lists of IDs.
        """
        list_1: list[int] = []
        list_2: list[int] = []

        with open(self._file_path, "r") as f:
            for line in f.readlines():
                num_1, num_2 = map(lambda num: int(num), line.split("   "))

                list_1.append(num_1)
                list_2.append(num_2)

        return list_1, list_2
