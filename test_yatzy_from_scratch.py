import pytest

import yatzy
from yatzy import Yatzy

# Chance
# The player scores the sum of all dice, no matter what they read.


def test_chance():
    # iterar sobre *args evita codigo cableado a 5 argumentos
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)


def test_ones():
    assert 5 == Yatzy.ones(1, 1, 1, 1, 1)
    assert 0 == Yatzy.ones(3, 3, 3, 4, 5)


def test_twos():
    assert 0 == Yatzy.twos(3, 3, 3, 4, 5)
    assert 4 == Yatzy.twos(2, 3, 2, 5, 1)


def test_threes():
    assert 0 == Yatzy.threes(1, 1, 1, 1, 1)
    assert 9 == Yatzy.threes(3, 3, 3, 4, 5)


@pytest.fixture
def inyector():
    # Es el setup de unittest o de JUnit
    tirada = Yatzy(4, 5, 6, 4, 5)
    return tirada


def test_fours(inyector):
  valorEsperado = 8
  assert valorEsperado == inyector.fours()


def test_fives(inyector):
    valorEsperado = 10
    assert valorEsperado == inyector.fives()


def test_sixes(inyector):
    valorEsperado = 6
    assert valorEsperado == inyector.sixes()


def test_pair():
    '''
    Pair:
    The player scores the sum of the two highest matching dice.
    '''
    # El algoritmo del metodo no es optimo, es complicado e ilegible.
    # La abstraccion, el nombre del metodo, no es adecuada
    # puesto que la categoria se llama pair.
    assert 8 == Yatzy.pair(3, 3, 3, 4, 4)
    assert 12 == Yatzy.pair(1, 1, 6, 2, 6)
    assert 6 == Yatzy.pair(3, 3, 3, 4, 1)
    assert 6 == Yatzy.pair(3, 3, 3, 3, 1)
    assert 0 == Yatzy.pair(1, 2, 3, 4, 5)


def test_two_pairs():
    '''
    Two pairs:
    If there are two pairs of dice with the same number, the
    player scores the sum of these dice.
    '''
    # La categoria se llama "two pairs": la abstraccion del metodo
    # no es adecuada.
    # Mantengo notacion snake_case
    # El algoritmo del metodo no es optimo, es complicado e ilegible.

    assert 8 == Yatzy.two_pairs(1, 1, 2, 3, 3)
    assert 0 == Yatzy.two_pairs(1, 1, 2, 3, 4)
    assert 6 == Yatzy.two_pairs(1, 1, 2, 2, 2)
    assert 0 == Yatzy.two_pairs(1, 2, 3, 4, 5)

def test_three_of_a_kind():
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 4, 5)
    assert 0 == Yatzy.three_of_a_kind(3, 3, 4, 5, 6)
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 3, 1)
    assert 0 == Yatzy.three_of_a_kind(1, 2, 3, 4, 5)


def test_four_of_a_kind():
    assert 8 == Yatzy.four_of_a_kind(2, 2, 2, 2, 5)
    assert 0 == Yatzy.four_of_a_kind(2, 2, 2, 5, 5)
    assert 8 == Yatzy.four_of_a_kind(2, 2, 2, 2, 2)
    assert 0 == Yatzy.four_of_a_kind(1, 2, 3, 4, 5)


def test_small_straight():
    assert 15 == Yatzy.small_straight(1, 2, 3, 4, 5)
    assert 0 == Yatzy.small_straight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.small_straight(1, 3, 4, 5, 5)
    assert 0 == Yatzy.small_straight(6, 6, 6, 6, 6)
    assert 0 == Yatzy.small_straight(1, 2, 3, 4, 6)


def test_large_straight(*dice):
    for numero in range(2, 7):
        if dice.count(numero) != 1:
            return 0
        return Yatzy.chance(*dice)


def test_fullHouse():
    assert 8 == Yatzy.fullHouse(1, 1, 2, 2, 2)
    assert 0 == Yatzy.fullHouse(2, 2, 3, 3, 4)
    assert 0 == Yatzy.fullHouse(4, 4, 4, 4, 4)
