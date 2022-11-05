import sys
sys.path.append('..')
from app.app import app
import pytest


@pytest.fixture
def client():
    return app.test_client()
