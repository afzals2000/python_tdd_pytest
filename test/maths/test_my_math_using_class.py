from maths.my_math import MathLib
import pytest
import sys


class TestMathLib:

    calc = MathLib()

    def setup_method(self):
        pass  # print("Set up to run before every test")

    @pytest.mark.parametrize("test_input, expected_output",
                             [
                                 (2, 4),
                                 (3, 9),
                                 (4, 16)
                             ]
                             )
    def test_square(self, test_input, expected_output):
        result = self.calc.square(test_input)
        assert result == expected_output

    @pytest.mark.parametrize("test_input1,test_input2, expected_output",
                             [
                                 (2, 3, 5),
                                 (4, 6, 10)
                             ]
                             )
    def test_add(self, test_input1, test_input2, expected_output):
        result = self.calc.add(test_input1, test_input2)
        assert result == expected_output

    @pytest.mark.skipif(sys.version_info > (3, 0), reason="Dont want to run on over then 3.0")
    def test_addskip(self):
        result = self.calc.add(2, 3)
        assert result == 5

    @pytest.mark.windows
    def test_add_on_windows(self):
        result = self.calc.add(2, 3)
        assert result == 5

    @pytest.mark.mac
    def test_add_on_mac(self):
        result = self.calc.add(2, 3)
        assert result == 5

    def teardown_method(self):
        pass  # print("Tear down to run after every test")

