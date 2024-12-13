"""
This is the file that houses the ID Connection class, for linking two IDs into a simple type.
"""


class IDConnection:
    def __init__(self, id_1: int, id_2: int) -> None:
        """
        A base class for the ID Location class. This was made to streamline the connection between two ID points for
        the AoC day 1 problem.
        :param id_1: An integer for ID 1
        :param id_2: An integer for ID 2
        """
        self._id_1: int = id_1
        self._id_2: int = id_2

        self._difference: int = abs(id_1 - id_2)

    @property
    def difference(self) -> int:
        """
        The difference property between the two given IDs. |ID 1 - ID 2|
        :return: The absolute difference between the 2 IDs.
        """
        return self._difference

    @property
    def id_1(self) -> int:
        """
        The first given ID        :return:  as an integer
        """
        return self._id_1

    @property
    def id_2(self) -> int:
        """
        The second given ID        :return:  as an integer
        """
        return self._id_2
