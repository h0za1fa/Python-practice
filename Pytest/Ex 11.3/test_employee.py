import pytest
from employee import Employee

@pytest.fixture

def employee():
    employee = Employee('hozaifa', 'naeem', 5000 )
    return employee

def test_give_default_raise(employee):
    salary = employee.salary
    employee.get_raise()
    assert employee.salary == salary + 5000

def test_give_custom_raise(employee):
    salary = employee.salary
    custom_raise = 55500
    employee.get_raise(raised= custom_raise)
    assert employee.salary == salary + custom_raise

