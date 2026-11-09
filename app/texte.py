
def nettoyer_texte(texte):
    if not isinstance(texte, str):
        raise TypeError("Texte attendu")
    return " ".join(texte.lower().split())
    
def test_nettoyer_texte_nombre():
    with pytest.raises(TypeError):
        nettoyer_texte(123)


def test_nettoyer_texte_none():
    with pytest.raises(TypeError):
        nettoyer_texte(None)
