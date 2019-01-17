from maths.my_math import MathLib
import pytest
import sys

pytest.calc = None


def setup_module():
    print("Set up")
    pytest.calc = MathLib()
    # open connection if any


@pytest.mark.parametrize("test_input, expected_output",
                         [
                             (2, 4),
                             (3, 9),
                             (4, 16)
                         ]
                         )
def test_square(test_input, expected_output):
    result = pytest.calc.square(test_input)
    assert result == expected_output


@pytest.mark.parametrize("test_input1,test_input2, expected_output",
                         [
                             (2, 3, 5),
                             (4, 6, 10)
                         ]
                         )
def test_add(test_input1, test_input2, expected_output):
    result = pytest.calc.add(test_input1, test_input2)
    assert result == expected_output


@pytest.mark.skipif(sys.version_info > (3, 0), reason="Dont want to run on over then 3.0")
def test_addskip():
    result = pytest.calc.add(2, 3)
    assert result == 5


@pytest.mark.windows
def test_add_on_windows():
    result = pytest.calc.add(2, 3)
    assert result == 5


@pytest.mark.mac
def test_add_on_mac():
    result = pytest.calc.add(2, 3)
    assert result == 5


def teardown_module():
    print("Tear Down")
    pytest.calc = None
    # close open connection if any

