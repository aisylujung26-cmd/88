import pytest

def test_first():
    assert 2+2 == 4
    assert 10-3 ==7
    assert 5*3 == 15

def test_string():
    name = "Ais"
    assert name == "Ais"
    assert len(name) == 3
    assert name.upper() == "AIS"

def test_list():
    num = [1,2,3]
    assert 2 in num
    assert len(num) == 3
    assert num[0] == 1


def add(a,b):
    return a+b

def is_even(num):
    return num % 2 == 0

def get_discount(price, discount_percent):
    return price- price*discount_percent/100

def test_add():
    assert add(2,3) == 5
    assert add(-1,2)==1
    assert add(0,0)==0


def test_is_even():
    assert is_even(6) is True
    assert is_even(8) is True
    assert is_even(9) is False

def test_discount():
    assert get_discount(100,20) == 80
    assert get_discount(100, 0) == 100

@pytest.mark.parametrize("a,b,expected", [
    (1,2,3),
    (4,5,9),
    (0,0,0),
    (-1,-1,-2)
])
def test_add_parametrize(a,b,expected):
    assert add(a,b) == expected


@pytest.mark.parametrize("num, expected", [
    (1,False),
    (2,True),
    (3,False),
    (4,True),
    (5,False),
])
def test_is_even_parametrize(num,expected):
    assert is_even(num) == expected

@pytest.fixture
def my_user():
    return {"name": "Ais", "age": 25, "email": "aisic@gmail.com",}

def test_user_name(my_user):
    assert my_user["name"] == "Ais"

def test_user_age(my_user):
    assert my_user["age"] == 25
    assert my_user["age"] > 17


def reverse_word(word):
    return word[::-1]


def test_reverse_word():
    assert reverse_word("aisi") == "isia"
    assert reverse_word("dog") == "god"
    assert reverse_word("cat") == "tac"


@pytest.mark.parametrize("word,expected", [
    ("sveta", "atevs"),
    ("12345", "54321"),
    ("marker", "rekram"),
])
def test_reverse_word_parametrize(word, expected):
    assert reverse_word(word) == expected


@pytest.fixture
def shopping_list():
    return ["milk","bread","coffee"]

def test_shopping_list(shopping_list):
    assert len(shopping_list) == 3
    assert shopping_list[0] == "milk"
    assert "bread" in shopping_list
    assert "apple" not in shopping_list

