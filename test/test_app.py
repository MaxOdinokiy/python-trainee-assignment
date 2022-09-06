from app.app import get_data, get_matrix, get_prepared_matrix, get_traversal_matrix
import asyncio

SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/' \
    'python-trainee-assignment/main/matrix.txt'

SOURCE_URL_2 = 'https://raw.githubusercontent.com/MaxOdinokiy/' \
    'python-trainee-assignment/main/test/fixtures/test_matrix_2.txt'

SOURCE_URL_3 = 'https://raw.githubusercontent.com/MaxOdinokiy/' \
    'python-trainee-assignment/ma/test/fixtures/test_matrix_2.txt'

TRAVERSAL = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]

PREPARED_MATRIX = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160],
]

PREPARED_MATRIX_2 = [
    [10, 20, 30, 40, 50],
    [60, 70, 80, 90, 100],
    [110, 120, 130, 140, 150],
    [160, 170, 180, 190, 200],
    [210, 220, 230, 240, 250],
]

TRAVERSAL_2 = [
    10, 60, 110, 160, 210,
    220, 230, 240, 250, 200,
    150, 100, 50, 40, 30,
    20, 70, 120, 170, 180,
    190, 140, 90, 80, 130,
]


def test_get_prepared_matrix():
    with open('test/fixtures/test_matrix.txt', 'r') as f:
        text = f.read()
    assert get_prepared_matrix(text) == PREPARED_MATRIX
    assert get_prepared_matrix('') == []


def test_get_traversal_matrix():
    assert get_traversal_matrix(PREPARED_MATRIX) == TRAVERSAL


def test_get_matrix():
    result = asyncio.run(get_matrix(SOURCE_URL))
    assert result == TRAVERSAL


def test_get_prepared_matrix_2():
    with open('test/fixtures/test_matrix_2.txt', 'r') as f:
        text = f.read()
    assert get_prepared_matrix(text) == PREPARED_MATRIX_2
    assert get_prepared_matrix('') == []


def test_get_traversal_matrix_2():
    assert get_traversal_matrix(PREPARED_MATRIX_2) == TRAVERSAL_2


def test_get_matrix_2():
    result = asyncio.run(get_matrix(SOURCE_URL_2))
    assert result == TRAVERSAL_2


def test_get_matrix_incorrect_url():
    result = asyncio.run(get_matrix(SOURCE_URL_3))
    assert result == []
