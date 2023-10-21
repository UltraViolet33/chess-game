

class Board:
    def __init__(self) -> None:
        self._board_array = []

    @property
    def board_array(self)-> list:
        print("hello")
        return self._board_array
    