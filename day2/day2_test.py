from unittest import TestCase, main
from day2 import solve


class TestDay2(TestCase):
    def test_solve_case0(self):
        self.assertEqual(solve(12.00, 20, 8), 15)

    def test_solve_case1(self):
        self.assertEqual(solve(15.50, 15, 10), 19)

    def test_solve_case2(self):
        self.assertEqual(solve(20.75, 10, 3), 23)

if __name__ == '__main__':
    main()