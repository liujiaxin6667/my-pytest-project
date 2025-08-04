import pytest
import yaml
def Add(a,b):
    return a+b

file_01 = open("yaml/data.yaml","r",encoding="utf-8")
list_01 = yaml.load(file_01,Loader=yaml.FullLoader)

class TestAdd:

    @pytest.mark.parametrize("dict_01",list_01)
    def test_add_01(self,dict_01):
        assert Add(dict_01["a"],dict_01["b"]) == dict_01["c"]
