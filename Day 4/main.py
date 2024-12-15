"""
URL: https://adventofcode.com/2024/day/4
"""
from parser import InputParser
from search_grid import WordSearchGrid
from utils import Utils


def main() -> None:
    """
    First gets the lines in the word search

    Part 1:
        Looks for all neighbours of the letter X in the grid, and if it finds the next letter in XMAS, continues down
        the same trajectory (treats the offset like a slope, and the length of XMAS like time) and either marks it
        as good if the word is completed, but if not doesn't count it.

    Part 2:
        Looks for the letter A in the grid, and if it finds it, looks at the X offsets. If they are 2 A's, and 2 S's,
        continues. If the letters diagonal don't equal each-other, it is counted.
    """
    grid: WordSearchGrid = WordSearchGrid(InputParser("input.txt").get_word_search_lines())

    # Part 1
    total_instances: int = 0
    for x in range(grid.width):
        for y in range(grid.height):
            pos = (x, y)
            if grid.get_char(pos) == "X":
                for offset in WordSearchGrid.NEIGHBOUR_OFFSETS:
                    found_segmented_word = ""
                    for i, letter in enumerate(WordSearchGrid.WORD_LOOKED_FOR):
                        letter = grid.get_char_from_offset(pos, Utils.multiply_tuple(offset, i))
                        if letter == WordSearchGrid.WORD_LOOKED_FOR[i]:
                            found_segmented_word += letter
                        else:
                            break
                    if found_segmented_word == WordSearchGrid.WORD_LOOKED_FOR:
                        total_instances += 1

    print(f"Total Instances: {total_instances}")

    # Entering Part 2
    print("\n|\n|\n| PART 2\n|\n|\n")

    total_x_instances: int = 0
    for x in range(grid.width):
        for y in range(grid.height):
            pos = (x, y)
            if grid.get_char(pos) == "A":
                letter_tracker = WordSearchGrid.LETTER_TRACKER_TEMPLATE.copy()
                for offset in WordSearchGrid.X_OFFSETS:
                    letter: dict[str: int] = grid.get_char_from_offset(pos, offset)
                    if letter:
                        letter_tracker[letter] += 1

                print(letter_tracker)
                if letter_tracker["M"] == 2 and letter_tracker["S"] == 2:
                    if grid.get_char_from_offset(pos, (-1, -1)) != grid.get_char_from_offset(pos, (1, 1)):
                        total_x_instances += 1

    print(f"Total instances of X-MAS: {total_x_instances}")


if __name__ == '__main__':
    main()
