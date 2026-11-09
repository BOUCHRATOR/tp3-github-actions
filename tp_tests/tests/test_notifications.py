import pytest
from app.notifications import envoyer_notification

def test_notification():

    with pytest.raises(RuntimeError):
        envoyer_notification("Bonjour")