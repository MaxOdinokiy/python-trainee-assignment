# Тестовое задание по python

## Условие

Необходимо реализовать Python-библиотеку, которая осуществляет получение квадратной матрицы (NxN) с удалённого сервера и возвращает её пользователю в виде `List[int]`. Этот список должен содержать результат обхода полученной матрицы по спирали: против часовой стрелки, начиная с левого верхнего угла (см. test case ниже).

Пример исходной матрицы:

```
+-----+-----+-----+-----+
|  10 |  20 |  30 |  40 |
+-----+-----+-----+-----+
|  50 |  60 |  70 |  80 |
+-----+-----+-----+-----+
|  90 | 100 | 110 | 120 |
+-----+-----+-----+-----+
| 130 | 140 | 150 | 160 |
+-----+-----+-----+-----+
```

Матрица гарантированно содержит целые неотрицательные числа. Форматирование границ иными символами не предполагается.

## Требования к выполнению и оформлению

- Библиотека содержит функцию со следующим интерфейсом:

    ```python
    async def get_matrix(url: str) -> List[int]:
        ...
    ```

- Функция единственным аргументом получает URL для загрузки матрицы с сервера по протоколу HTTP(S).
Done
- Функция возвращает список, содержащий результат обхода полученной матрицы по спирали: против часовой стрелки, начиная с левого верхнего угла.
Done
- Взаимодействие с сервером должно быть реализовано асинхронно - посредством aiohttp, httpx или другого компонента на asyncio.
Done
- Библиотека должна корректно обрабатывать ошибки сервера и сетевые ошибки (5xx, Connection Timeout, Connection Refused, ...).
- В дальнейшем размерность матрицы может быть изменена с сохранением форматирования. Библиотека должна сохранить свою работоспособность на квадратных матрицах другой размерности.
- Решение задачи необходимо разместить на одном из публичных git-хостингов (GitHub, GitLab, Bitbucket). Можно также выслать решение в виде архива (zip, tar). Загружать библиотеку в PyPi или другие репозитории не требуется. Done

## Проверка решения

- Для самостоятельной проверки можно использовать следующий test case:

    ```python
    SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
    TRAVERSAL = [
        10, 50, 90, 130,
        140, 150, 160, 120,
        80, 40, 30, 20,
        60, 100, 110, 70,
    ]

    def test_get_matrix():
        assert asyncio.run(get_matrix(SOURCE_URL)) == TRAVERSAL
    ```

При проверке мы также будем обращать внимание на тесты, type hints, структуру решения и общее качество кода.

Удачи в выполнении задачи и не забывайте о [The Zen of Python](https://www.python.org/dev/peps/pep-0020/#the-zen-of-python)! :)