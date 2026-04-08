import pytest
from binaire.bit import Bit

def test_bit_str():
    assert str(Bit.BIT_0) == "0"
    assert str(Bit.BIT_1) == "1"

def test_bit_repr():
    assert repr(Bit.BIT_0) == "Bit.BIT_0"
    assert repr(Bit.BIT_1) == "Bit.BIT_1"