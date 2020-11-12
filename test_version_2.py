import pytest 
from  bloom2 import Bloom2

'''
    test case for Bloom2 
'''
class TestBloom2:

    @classmethod
    @pytest.fixture(scope='class', autouse=True)
    def setup_class(cls):
        pass


    def test_2mb_file(self):
        f = open("data/sample-2mb-text.txt", "r")
        sample = f.read()

        lines = sample.splitlines()
        mb = Bloom2()
        false_positive = 0

        for line  in lines:
            if not mb.Add(line):
                false_positive += 1

        assert false_positive==1
        assert mb.Len()==2850

    def test_emerson(self):
        f = open("data/emerson_essays.txt", "r")
        sample = f.read()

        lines = sample.splitlines()
        mb = Bloom2()
        false_positive = 0

        for line  in lines:
            if not  mb.Add(line):
                false_positive += 1

        assert false_positive==1458
        assert mb.Len()==8772