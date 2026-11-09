
import pytest
from app.texte import nettoyer_texte

@pytest.mark.parametrize("entree, attendu", [
    ("  Bonjour  monde", "bonjour monde"),
    ("HELLO", "hello"),
    ("  World  ", "world")
])
def test_nettoyer_texte(entree, attendu):
    assert nettoyer_texte(entree) == attendu
