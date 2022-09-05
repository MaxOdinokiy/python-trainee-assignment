from app.app import get_data, get_matrix, get_prepared_matrix, get_traversal_matrix
import asyncio

SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/ \
    python-trainee-assignment/main/matrix.txt'

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


def test_get_prepared_matrix():
    with open('fixtures/test_matrix.txt', 'r') as f:
        text = f.open()
    assert get_prepared_matrix(text) == PREPARED_MATRIX
    assert get_prepared_matrix('') == []


def test_get_traversal_matrix():
    assert get_traversal_matrix(PREPARED_MATRIX) == TRAVERSAL


def test_get_matrix():
    assert asyncio.run(get_matrix(SOURCE_URL)) == TRAVERSAL
