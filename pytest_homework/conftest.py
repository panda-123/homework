#ecoding=utf-8
# author:herui
# time:2020/12/14 13:59
# function: 实现执行案例后，参数化中的中文不能正常显示的问题

import pytest
import yaml

from .pythoncode.calculator import Calculator


@pytest.fixture(scope="module")
def start():
    calc = Calculator()
    print("开始计算")
    yield calc
    print("结束计算")


def pytest_collection_modifyitems(session, config, items):
    # print("item的类型是：",type(items))
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        # if "add" in item._nodeid:
        #     item.add_marker(pytest.mark.add)
        # if "div" in item._nodeid:
        #     item.add_marker(pytest.mark.div)