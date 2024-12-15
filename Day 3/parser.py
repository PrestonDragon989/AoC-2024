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
            return False

        else:
            split_mul: list[str] = mul_string.split(",")
            return [int(split_mul[0].split("(", 1)[1]), int(split_mul[1].split(")", 1)[0])]

    @staticmethod
    def _reset_input_string_mul_start(file_text: str, check_character: str) -> str or False:
        """
        Simply reset the file for the next mul scan.
        @param file_text: The text of the un-reset file.
        @return: New reset file, or false if it can't reset (no valid index for 'mul')
        """
        try:
            start_index = file_text.index(check_character)
            return file_text[start_index:]
        except ValueError:
            return False

    @staticmethod
    def _remove_substring(original_string: str, index_1: int, index_2: int) -> str:
        """
        Cuts out a section of a string, from index 1 to index 2.
        @return:
        @param original_string: Original Given string to cut out of
        @param index_1: First given index
        @param index_2: Second Given Index
        """
        return original_string[:index_1] + original_string[index_2:]

    def _get_parsed_mul_strings(self, mul_strings: list[str]) -> list[list[int, int]]:
        """
        Parses mul string, and returns a list of the numbers obtained from them.
        @param mul_strings: A list of the raw mul strings.
        @return: A list of the mul parameters.
        """
        mul_numbers: list[list[int, int]] = []
        for raw_string in mul_strings:
            valid: bool or list[int, int] = self._valid_mul_string(raw_string)
            if valid:
                mul_numbers.append(valid)

        return mul_numbers

    def get_mul_numbers(self) -> list[list[int, int]]:
        """
        Scans the contents of the given file for all instances of mul(x,x), using _reset_input_string_mul_start and
        _valid_mul_string to reset and check.
        @return: A list of number sets to multiply, taken from the input file
        """
        mul_raw_strings: list[str] = []

        with open(self._file_path, "r") as f:
            file_text: str or bool = self._reset_input_string_mul_start(f.read().replace("\n", ""), "mul(")
            if not file_text:
                return []

            while True:
                try:
                    mul_index: int = file_text.index("mul(")
                    end_index: int = file_text.index(")")
                    mul_string: str = file_text[mul_index:end_index + 1]

                    mul_raw_strings.append(mul_string)

                    # Checking correct mul statements in found ones
                    if mul_string.count("mul(") > 1:
                        mul_raw_strings.pop(-1)
                        file_text = self._reset_input_string_mul_start(file_text[mul_index + 1:], "mul(")
                        continue

                    file_text = self._reset_input_string_mul_start(file_text[end_index - 1:], "mul(")
                    if not file_text:
                        break

                except ValueError:
                    break

        # Parsing strings
        return self._get_parsed_mul_strings(mul_raw_strings)

    def get_do_check_mul_numbers(self) -> list[list[int, int]]:
        """
        Does what get_mul_numbers does, except it checks for do() and don't(). If it says do(), all valid mul statements
        are usable. If it says don't(), then everything afterword is un-usable until stated otherwise.
        @return: List of mul parameters that got through checks
        """
        mul_raw_strings: list[str] = []

        do: bool = True

        with open(self._file_path, "r") as f:
            file_text: str = f.read().replace("\n", "")

            while True:
                # Attempting to get mul statements. If it can't find any, break out & return.
                try:
                    mul_index: int = file_text.index("mul(")
                    end_index: int = file_text[mul_index:].index(")") + mul_index
                except ValueError:
                    break

                # Getting nearest indexes of do and don't.
                try:
                    do_index: int = file_text.index("do()")
                except ValueError:
                    # if there is no longer a do, but there was a don't, the rest doesn't need to be parsed, return.
                    if not do:
                        break

                try:
                    dont_index: int = file_text.index("don't()")
                except ValueError:
                    pass

                # Get the nearest do after the don't. If there is none, return (no need to parse after)
                if dont_index < mul_index:
                    while True:
                        if do_index > dont_index:
                            file_text = file_text[max(do_index, dont_index) + 1:]
                            break
                        else:
                            file_text = self._remove_substring(file_text, do_index, do_index + 1)
                            try:
                                do_index = file_text.index("do()")
                            except ValueError:
                                return self._get_parsed_mul_strings(mul_raw_strings)
                            dont_index = file_text.index("don't()")
                    continue

                mul_string: str = file_text[mul_index:end_index + 1]
                mul_raw_strings.append(mul_string)

                # Checking correct mul statements in found ones
                if mul_string.count("mul(") > 1:
                    mul_raw_strings.pop(-1)
                    file_text = self._reset_input_string_mul_start(file_text[mul_index + 1:], "mul(")
                    continue

                file_text = self._remove_substring(file_text, mul_index, end_index + 1)  # Cutting out last mul

        return self._get_parsed_mul_strings(mul_raw_strings)
