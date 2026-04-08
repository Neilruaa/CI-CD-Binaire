import pytest
from binaire.bit import Bit
from binaire.code_binaire import CodeBinaire


@pytest.fixture
def code_base():
    return CodeBinaire(Bit.BIT_1, Bit.BIT_0, Bit.BIT_1)


def test_initialisation_et_proprietes(code_base):
    assert len(code_base) == 3
    assert code_base.bits == (Bit.BIT_1, Bit.BIT_0, Bit.BIT_1)


def test_ajouter(code_base):
    code_base.ajouter(Bit.BIT_0)
    assert len(code_base) == 4
    assert code_base[-1] == Bit.BIT_0


@pytest.mark.parametrize("bits, resultat_attendu", [
    ([Bit.BIT_0], "0"),
    ([Bit.BIT_1, Bit.BIT_1], "11"),
    ([Bit.BIT_0, Bit.BIT_1, Bit.BIT_0], "010")
])

def test_str_affichage(bits, resultat_attendu):
    cb = CodeBinaire(*bits)
    assert str(cb) == resultat_attendu


def test_addition(code_base):
    autre_code = CodeBinaire(Bit.BIT_0)
    resultat = code_base + autre_code
    assert str(resultat) == "1010"
    assert len(resultat) == 4

    assert str(code_base) == "101"


def test_addition_erreur(code_base):
    with pytest.raises(TypeError):
        code_base + "Ceci n'est pas un CodeBinaire"


def test_egalite(code_base):
    code_identique = CodeBinaire(Bit.BIT_1, Bit.BIT_0, Bit.BIT_1)
    code_different = CodeBinaire(Bit.BIT_1, Bit.BIT_1)

    assert code_base == code_identique
    assert code_base != code_different
    assert code_base != "101"


def test_getitem(code_base):
    assert code_base[0] == Bit.BIT_1
    assert code_base[1] == Bit.BIT_0

    slice_cb = code_base[0:2]
    assert isinstance(slice_cb, CodeBinaire)
    assert str(slice_cb) == "10"


def test_setitem(code_base):
    code_base[1] = Bit.BIT_1
    assert str(code_base) == "111"


def test_delitem(code_base):
    del code_base[1]
    assert len(code_base) == 2
    assert str(code_base) == "11"


def test_and_logique():
    cb1 = CodeBinaire(Bit.BIT_1, Bit.BIT_0, Bit.BIT_1)  # 101
    cb2 = CodeBinaire(Bit.BIT_1, Bit.BIT_1, Bit.BIT_0)  # 110

    resultat = cb1 & cb2
    assert str(resultat) == "100"


def test_or_logique():
    cb1 = CodeBinaire(Bit.BIT_1, Bit.BIT_0, Bit.BIT_1)  # 101
    cb2 = CodeBinaire(Bit.BIT_1, Bit.BIT_1, Bit.BIT_0)  # 110

    resultat = cb1 | cb2
    assert str(resultat) == "111"


def test_operations_erreur_longueur():
    cb1 = CodeBinaire(Bit.BIT_1)
    cb2 = CodeBinaire(Bit.BIT_1, Bit.BIT_0)

    with pytest.raises(ValueError):
        cb1 & cb2