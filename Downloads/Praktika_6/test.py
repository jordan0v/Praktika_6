import unittest
from main import *

class TestResult(unittest.TestCase):

    def test_res(self):
        func_res = isAllThreeInRow()
        self.assertEqual((False, ''), func_res)

    def test_res_column(self):
        func_res = isAllThreeInColumn()
        self.assertEqual((False, ''), func_res)

    def test_res_diagonal(self):
        func_res = isAllThreeDiagonal()
        self.assertEqual((False, ''), func_res)

    def test_res_draw(self):
        func_res = isAllThreeDiagonal()
        self.assertEqual((False, ''), func_res)

    def test_res_game(self):
        func_res = isGameOver()
        self.assertEqual((False, ''), func_res)

