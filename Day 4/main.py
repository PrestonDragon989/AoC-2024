"""
URL: https://adventofcode.com/2024/day/4
"""
from parser import InputParser
from search_grid import WordSearchGrid
from utils import Utils


def main() -> None:
    """
    First gets the lines in the word search
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


if __name__ == '__main__':
    main()
