import pytest
from main import format_address

def test_city_country():
    """test if the out put is properly formatted"""
    address = format_address('santiago','chile')
    assert address == 'Santiago, Chile'