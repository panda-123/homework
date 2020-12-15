#ecoding=utf-8
# author:herui
# time:2020/12/15 17:51
# function:
# 1、数据驱动实现
# 2、使用fixture替换setup和teardown，且放在conftest.py文件中
# 3、修改运行规则，pytest.ini文件
import allure
import pytest
import yaml


def get_data(key):
    print("执行myfixture")
    with open("./data.yml",encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        if key in ["adddatas", "myids", "divdatas", "muldatas", "subdatas"]:
            print(datas[key])
            return datas[key]

@allure.suite("计算器")
class TestCalcByParam:

    @pytest.mark.run(order=1)
    @allure.sub_suite("加法")
    @allure.story("加法")
    @pytest.mark.add
    @pytest.mark.parametrize("a,b,expect", get_data("adddatas"), ids=get_data("myids"))
    def test_add(self, start, a, b, expect):
        assert expect == start.add(a, b)

    @allure.sub_suite("减法")
    @allure.story("减法")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expect", get_data("subdatas"), ids=get_data("myids"))
    @pytest.mark.sub
    def test_sub(self, start, a, b, expect):
        assert expect == round(start.sub(a, b),2)

    @allure.sub_suite("乘法")
    @allure.story("乘法")
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a,b,expect", get_data("muldatas"), ids=get_data("myids"))
    @pytest.mark.mul
    def test_mul(self, start, a, b, expect):
        assert expect == start.mul(a, b)

    @allure.sub_suite("除法")
    @allure.story("除法")
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a,b,expect", get_data("divdatas"), ids=get_data("myids"))
    @pytest.mark.div
    def test_div(self, start, a, b, expect):
        assert expect == start.div(a, b)


