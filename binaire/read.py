from .bit import Bit
from .code_binaire import CodeBinaire

def lire_fichier_binaire(chemin_fichier: str) -> CodeBinaire:
    with open(chemin_fichier, 'r', encoding='utf-8') as f:
        contenu = f.read().strip()

    bits = []
    for caractere in contenu:
        if caractere == '0':
            bits.append(Bit.BIT_0)
        elif caractere == '1':
            bits.append(Bit.BIT_1)

    if not bits:
        raise ValueError("Le fichier ne contient aucun bit valide.")

    return CodeBinaire(*bits)