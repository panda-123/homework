import pytest
from .pythoncode.calculator import Calculator


class TestCalc:
    def setup_method(self):
        self.calc = Calculator()
        print("开始计算")

    def teardown_method(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expect", [
        (3, 5, 8), (-1, -2, -3), (100, 300, 400),(0.01,0.15,0.16)
    ], ids=["int", "minus", "bigint","float"])
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (5, 3, 2), (-1, -2, 1), (-100, 300, -400), (0.01, 0.15, -0.14)
    ], ids=["int", "minus", "bigint", "float"])
    def test_sub(self, a, b, expect):
        assert expect == round(self.calc.sub(a, b),2)

    @pytest.mark.parametrize("a,b,expect", [
        (5, 3, 15), (-1, -2, 2), (-100, 300, -30000), (0.01, 0.15, 0.0015),(0,23,0)
    ], ids=["int", "minus", "bigint", "float", "zero"])
    def test_mul(self, a, b, expect):
        assert expect == self.calc.mul(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (3, 5, 0.6), (-1, -2, 0.5), (-100, 300, -0.33), (0.03, 0.15, 0.2),(0,0.1,0),(1,0,"分母不能为0")
    ], ids=["int", "minus", "bigint", "float","zero", "error"])
    def test_div(self, a, b, expect):
        assert expect == self.calc.div(a, b)
