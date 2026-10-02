import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.app import app


def test_home_page():
    """Bosh sahifa 200 qaytarishi kerak"""
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'CI/CD Demo' in response.data


def test_health_endpoint():
    """Health endpoint ishlashi kerak"""
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'ok'


def test_404_page():
    """Mavjud bo'lmagan sahifa 404 qaytarishi kerak"""
    client = app.test_client()
    response = client.get('/mavjud-emas')
    assert response.status_code == 404
