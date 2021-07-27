from typing import List
import unittest
from unittest.loader import makeSuite

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

    def test_is_odd_00(self) -> None:
        actual: bool = main.is_odd(x=0)
        self.assertFalse(actual)

    def test_is_odd_01(self) -> None:
        actual: bool = main.is_odd(x=1)
        self.assertTrue(actual)

    def test_is_odd_02(self) -> None:
        actual: bool = main.is_odd(x=1563)
        self.assertTrue(actual)

    def test_is_odd_03(self) -> None:
        actual: bool = main.is_odd(x=-1563)
        self.assertTrue(actual)

    def test_is_odd_04(self) -> None:
        actual: bool = main.is_odd(x=-15632)
        self.assertFalse(actual)

    def test_is_odd_05(self) -> None:
        actual: bool = main.is_odd(x=15632)
        self.assertFalse(actual)

    def test_is_odd_06(self) -> None:
        actual: bool = main.is_odd(x=4)
        self.assertFalse(actual)

    def test_count_odd_numbers_00(self) -> None:
        actual: int = main.count_odd_numbers(xs=[])
        expected: int = 0
        self.assertEqual(first=expected, second=actual)

    def test_count_odd_numbers_01(self) -> None:
        actual: int = main.count_odd_numbers(xs=[1])
        expected: int = 1
        self.assertEqual(first=expected, second=actual)

    def test_count_odd_numbers_02(self) -> None:
        actual: int = main.count_odd_numbers(xs=[1, 3])
        expected: int = 2
        self.assertEqual(first=expected, second=actual)

    def test_count_odd_numbers_03(self) -> None:
        actual: int = main.count_odd_numbers(xs=[2])
        expected: int = 0
        self.assertEqual(first=expected, second=actual)

    def test_count_odd_numbers_04(self) -> None:
        actual: int = main.count_odd_numbers(xs=[2, 22])
        expected: int = 0
        self.assertEqual(first=expected, second=actual)

    def test_count_odd_numbers_05(self) -> None:
        actual: int = main.count_odd_numbers(xs=[2, 22, -46])
        expected: int = 0
        self.assertEqual(first=expected, second=actual)

    def test_count_odd_numbers_06(self) -> None:
        actual: int = main.count_odd_numbers(xs=[1, 2, 22, 333, -46, -11])
        expected: int = 3
        self.assertEqual(first=expected, second=actual)

    def test_list_of_floors_00(self) -> None:
        actual: List[int] = main.list_of_floors(m=0, n=0)
        expected: List[int] = []
        self.assertEqual(first=actual, second=expected)

    def test_list_of_floors_01(self) -> None:
        actual: List[int] = main.list_of_floors(m=1, n=1)
        expected: List[int] = []
        self.assertEqual(first=actual, second=expected)

    def test_list_of_floors_02(self) -> None:
        actual: List[int] = main.list_of_floors(m=1, n=2)
        expected: List[int] = [1]
        self.assertEqual(first=actual, second=expected)

    def test_list_of_floors_03(self) -> None:
        actual: List[int] = main.list_of_floors(m=2, n=3)
        expected: List[int] = [1]
        self.assertEqual(first=actual, second=expected)

    def test_list_of_floors_04(self) -> None:
        actual: List[int] = main.list_of_floors(m=2, n=4)
        expected: List[int] = [1, 1, 0, 1]
        self.assertEqual(first=actual, second=expected)

    def test_list_of_floors_05(self) -> None:
        actual: List[int] = main.list_of_floors(m=1, n=3)
        expected: List[int] = [1, 2, 0, 1]
        self.assertEqual(first=actual, second=expected)
