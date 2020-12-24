import pytest
import yaml

def get_data(key):
    print("执行myfixture")
    with open("./data.yml",encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        if key in ["adddatas", "myids", "divdatas", "muldatas", "subdatas"]:
            print(datas[key])
            return datas[key]

class TestCalcByFixture:

    @pytest.mark.add
    @pytest.mark.parametrize("a,b,expect",
                             get_data("adddatas"),
                             ids=get_data("myids"))
    def test_add(self, start, a,b,expect):
        assert expect == start.add(a, b)

    @pytest.mark.parametrize("a,b,expect",
                             get_data("subdatas"),
                             ids=get_data("myids"))
    @pytest.mark.sub
    def test_sub(self, start, a, b, expect):
        assert expect == round(start.sub(a, b),2)

    @pytest.mark.parametrize("a,b,expect",
                             get_data("muldatas"),
                             ids=get_data("myids"))
    @pytest.mark.mul
    def test_mul(self, start, a, b, expect):
        assert expect == start.mul(a, b)

    @pytest.mark.parametrize("a,b,expect",
                             get_data("divdatas"),
                             ids=get_data("myids"))
    @pytest.mark.div
    def test_div(self, start, a, b, expect):
        assert expect == start.div(a, b)
