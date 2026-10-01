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
