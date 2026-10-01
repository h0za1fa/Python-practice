import pytest
from main import format_address

def test_city_country():
    """test if the out put is properly formatted"""
    address = format_address('santiago','chile')
    assert address == 'Santiago, Chile'

def test_city_population():
    """test if population is displayed and formatted properly"""
    address = format_address('santiago', 'chile', 10000)
    assert address == 'Santiago, Chile - Population: 10000'