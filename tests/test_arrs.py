from utils import arrs
import pytest
def test2_get():
    with pytest.raises(IndexError):
        assert arrs.get([], 0, "test")
        assert arrs.get([1, 2, 3], -2, "test") == ["test"]


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -4) == [ 1, 2, 3]
    assert arrs.my_slice([1, 2, 3], -2) == [2, 3]