import pytest
import yaml


def func(x):
    return x+1


def test_answer():
    assert func(3) == 4, '返回参数加一值'


class TestMethod:
    @pytest.mark.parametrize("env", yaml.safe_load(open('env.yml')))
    def test_one(self, env):
        if 'test' in env:
            print('这是测试环境',env['test'])
        if 'dev' in env:
            print('这是开发环境', env['dev'])

    def test_ymlrd(self):
        print(yaml.safe_load(open('env.yml')))


    # def test_three(self):
    #     x = "hello"
    #     assert hasattr(x, "lower")


