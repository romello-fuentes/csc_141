# 11-3, employee, pg 261


import pytest
from test_employee import Employee

@pytest.fixture
def sample_employee():
    return Employee('Alex', 'Taylor', 50000)

def test_give_default_raise(sample_employee):
    sample_employee.give_raise()
    assert sample_employee.annual_salary == 55000

def test_give_custom_raise(sample_employee):
    sample_employee.give_raise(8000)
    assert sample_employee.annual_salary == 58000
