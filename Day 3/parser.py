"""
The class for the parser, to get the instructions from the input (input.txt) file.
"""
import re


class InputParser:
    _string_numbers = list(map(lambda n: str(n), range(0, 10)))
    _filler_character = "x"
    _base_mul_string = f"mul({_filler_character},{_filler_character})"

    def __init__(self, file_path: str) -> None:
        self._file_path: str = file_path

    def _valid_mul_string(self, mul_string: str) -> bool or list[int, int]:
        """
        Checks to make sure the given string is valid for mul(x,x). It first parses the numbers of the expression, then
        makes sure that what it got was correct. Then it collects the numbers to return.
        @param mul_string: The string to parse
        @return: If string isn't valid, False. if it is, the two numbers to multiply (mul)
        """
        if self._filler_character in mul_string:
            return False

        # Regex: Replaces all numbers with the filler character (_filler_character)
        num_removed_string = re.sub(r'\d', self._filler_character, mul_string)

        # Regex: takes all clusters of x that are above on and turns them to one. (ex: "xx fds j xxx" => "x fds j x"
        # Used to simplify the mul expression to check if it matches the placeholder one (_base_mul_string)
        num_removed_string: str = re.sub(f'({self._filler_character})+', lambda m: m.group(1), num_removed_string)
        if num_removed_string != self._base_mul_string:
            # print(mul_string)
            return False

        else:
            split_mul: list[str] = mul_string.split(",")
            return [int(split_mul[0].split("(", 1)[1]), int(split_mul[1].split(")", 1)[0])]

    @staticmethod
    def _reset_input_string_mul_start(file_text) -> str or False:
        """
        Simply reset the file for the next mul scan.
        @param file_text: The text of the un-reset file.
        @return: New reset file, or false if it can't reset (no valid index for 'mul')
        """
        try:
            start_index = file_text.index("mul")
            return file_text[start_index:]
        except ValueError:
            return False

    def get_mul_numbers(self) -> list[list[int, int]]:
        """
        Scans the contents of the given file for all instances of mul(x,x), using _reset_input_string_mul_start and
        _valid_mul_string to reset and check.
        @return: A list of number sets to multiply, taken from the input file
        """
        mul_numbers: list[list[int, int]] = []
        mul_raw_strings: list[str] = []

        with open(self._file_path, "r") as f:
            file_text: str or bool = self._reset_input_string_mul_start(f.read().replace("\n", ""))
            if not file_text:
                return mul_numbers

            while True:
                try:
                    mul_index: int = file_text.index("mul(")
                    end_index: int = file_text.index(")")
                    mul_string: str = file_text[mul_index:end_index + 1]

                    mul_raw_strings.append(mul_string)

                    # Checking correct mul statements in found ones
                    if mul_string.count("mul(") > 1:
                        mul_raw_strings.pop(-1)
                        file_text = self._reset_input_string_mul_start(file_text[mul_index + 1:])
                        continue

                    file_text = self._reset_input_string_mul_start(file_text[end_index - 1:])
                    if not file_text:
                        break

                except ValueError:
                    break

        # Parsing strings
        for raw_string in mul_raw_strings:
            valid: bool or list[int, int] = self._valid_mul_string(raw_string)
            if valid:
                mul_numbers.append(valid)

        return mul_numbers
