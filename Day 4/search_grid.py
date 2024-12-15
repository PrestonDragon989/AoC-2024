"""
Base file for the class WordSearchGrid. It is used as an easier way to manage the word search as a grid.
"""
from utils import Utils


class WordSearchGrid:
    """
    Neighbour Offsets: Used for part 1 when scanning all the letters adjacent to X, and the used as trajectory/slope
    X Offsets: Used in part 2 to see all nearby letters, and if they equal the correct things.
    Word Looked For: This is the word that is being looked for in the word search (For Part 1)
    Letter Tracker Template: A simple template, made to be copied, that holds all the letters of the looked for word.
    """
    NEIGHBOUR_OFFSETS: list[tuple] = [
        (-1, 1),  (0, 1),  (1, 1),
        (-1, 0),  (0, 0),  (1, 0),
        (-1, -1), (0, -1), (1, -1)
    ]

    X_OFFSETS: list[tuple] = {
        (1,  -1),  (1,  1),
        (-1, -1),  (-1, 1)
    }

    WORD_LOOKED_FOR = "XMAS"
    LETTER_TRACKER_TEMPLATE = {
        "X": 0,
        "M": 0,
        "A": 0,
        "S": 0
    }

    def __init__(self, search_list: list[str]):
        self._raw_lines: list[str] = search_list

        self._width: int = len(self._raw_lines[0])
        self._height: int = len(self._raw_lines)

        self._search_grid = self._convert_lines_to_grid(self._raw_lines)

    def get_char_from_offset(self, pos: tuple, offset: tuple) -> str or False:
        """
        Used to get a letter from a start position and an offset.
        @param pos: Start coordinate
        @param offset: Offset of start coordinate
        @return: Either the coordinate obtained from the offset, or False if location doesn't exist
        """
        location = Utils.add_tuples(pos, offset)

        if location in self._search_grid:
            return self._search_grid[location]

        return False

    def get_char(self, pos: tuple[int, int]) -> str or False:
        """
        Used for getting specific characters
        @param pos: Coordinate in grid
        @return: Either the character at the location, or False if it doesn't exist.
        """
        if pos in self._search_grid:
            return self._search_grid[pos]

        return False

    @property
    def width(self) -> int:
        """
        The width of the grid.
        @return: Grid width as an integer
        """
        return self._width

    @property
    def height(self) -> int:
        """
        The height of the grid.
        @return: Grid height as an integer
        """
        return self._height

    @staticmethod
    def _convert_lines_to_grid(lines: list[str]) -> dict[tuple[int, int]: str]:
        """
        Maps all the word search letters to a grid that uses X and Y.
        @return: A dictionary (grid) of word search letters
        """
        word_search_grid = {}
        for y, line in enumerate(lines):
            for x, letter in enumerate(line):
                word_search_grid[(x, y)] = letter

        return word_search_grid
