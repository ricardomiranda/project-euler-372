import unittest

from app import main


class TestMain(unittest.TestCase):
    def test_floor_division_squares_00(self) -> None:
        actual: int = main.floor_division_squares(x=1, y=1)
        expected: int = 1

        self.assertEqual(first=expected, second=actual)

    def test_floor_division_squares_01(self) -> None:
        self.assertRaises(ZeroDivisionError,
                          main.floor_division_squares, x=0, y=0)

    def test_floor_division_squares_02(self) -> None:
        actual: int = main.floor_division_squares(x=2, y=2)
        expected: int = 1

        self.assertEqual(first=expected, second=actual)

    def test_floor_division_squares_03(self) -> None:
        actual: int = main.floor_division_squares(x=1, y=2)
        expected: int = 4

        self.assertEqual(first=expected, second=actual)

    def test_floor_division_squares_04(self) -> None:
        actual: int = main.floor_division_squares(x=2, y=3)
        expected: int = 2

        self.assertEqual(first=expected, second=actual)
