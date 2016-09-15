import pytest
import tdd

def test_chemeq():
    assert Kd == Ca*Cb/Cab
    assert Ca0 == Ca + Cab
    assert Cb0 == Cb + Cab


    pytest.raises(RuntimeError, "tdd.n_neg('Z')")
    return None
