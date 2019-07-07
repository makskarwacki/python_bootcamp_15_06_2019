def podnies_do_potegi(x, y=2, z=""):
    return x**y


def test_podnies_do_potegi():
    assert podnies_do_potegi(2) == 4
    assert podnies_do_potegi(3) == 9
    assert podnies_do_potegi(2, 3) == 8
    assert podnies_do_potegi(3, 3) == 27
