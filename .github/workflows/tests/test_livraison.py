from app.livraison import frais_livraison

def test_livraison_panier_ordinaire():
    # Arrange
    montant = 120
    # Act
    resultat = frais_livraison(montant)
    # Assert
    assert resultat == 25
def test_livraison_299():
    assert frais_livraison(299) == 25
def test_livraison_300():
    assert frais_livraison(300) == 0
def test_livraison_301():
    assert frais_livraison(301) == 0
def test_livraison_negatif():
    assert frais_livraison(0)==25