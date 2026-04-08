import pytest
from binaire.bit import Bit
from binaire.read import lire_fichier_binaire


def test_lire_fichier_binaire_avec_mock(mocker):
    contenu_simule = "1101"
    mock_open = mocker.patch("builtins.open", mocker.mock_open(read_data=contenu_simule))
    faux_chemin = "dossier_imaginaire/test_data.txt"
    resultat = lire_fichier_binaire(faux_chemin)
    mock_open.assert_called_once_with(faux_chemin, 'r', encoding='utf-8')
    assert len(resultat) == 4
    assert str(resultat) == "1101"
    assert resultat[0] == Bit.BIT_1
    assert resultat[-1] == Bit.BIT_1