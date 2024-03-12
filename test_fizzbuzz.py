import pytest
from fizzbuzz import FizzBuzz

@pytest.fixture
def fb():
    return FizzBuzz()

def test_1to1(fb):
    assert "1" == fb.generate(1, 1)

def test_17to17(fb):
    assert "17" == fb.generate(17, 17)

def test_3toFizz(fb):
    assert "Fizz" == fb.generate(3, 3)

def test_12toFizz(fb):
    assert "Fizz" == fb.generate(12, 12)

def test_5toBuzz(fb):
    assert "Buzz" == fb.generate(5, 5)

def test_25toBuzz(fb):
    assert "Buzz" == fb.generate(25, 25)

def test_15toFizzBuzz(fb):
    assert "FizzBuzz" == fb.generate(15, 15)

def test_45toFizzBuzz(fb):
    assert "FizzBuzz" == fb.generate(45, 45)

def test_2range5to2Fizz4Buzz(fb):
    assert "2Fizz4Buzz" == fb.generate(2, 5)

def test_45range52to2Fizz4Buzz(fb):
    assert "FizzBuzz4647Fizz49BuzzFizz52" == fb.generate(45, 52)


