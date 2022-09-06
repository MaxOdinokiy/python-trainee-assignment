from typing import List
from aiohttp import web, ClientError
import asyncio
import aiohttp
import logging

SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/' \
    'python-trainee-assignment/main/matrix.txt'

logger = logging.getLogger(__name__)

async def get_data(url: str) -> str:
    try:
        conn = aiohttp.TCPConnector()
        async with aiohttp.ClientSession(connector=conn) as session:
            async with session.get(url, ssl=False) as response:
                if 400 <= response.status < 500:
                    logger.error("Client error")
                elif response.status > 500:
                    logger.error("server error")
                else:
                    return await response.text()
    except ClientError as ex:
        logger.error(f"There are problems with connection {ex}")
    except TimeoutError as ex:
        logger.error(f"Timeout error {ex}")


def get_prepared_matrix(source: str) -> List[List[int]]:
    try:
        output_matrix = []
        for line in source.split('\n'):
            if line and line[0] != '+':
                output_matrix.append(
                    [int(num) for num in line[1:-1].replace(' ', '').split('|')]
                    )
    except AttributeError as ex:
        logger.warning(ex)
    return output_matrix

def get_traversal_matrix(matrix: List[List[int]]) -> List[int]:
    output = []
    def walk(matrix, output):
        if not len(matrix):
            return output
        matrix = list(zip(*matrix[::-1]))
        output.extend(matrix[0][::-1])
        return walk(matrix[1:], output)
    return walk(matrix, output)


async def get_matrix(url: str) -> List[int]:
    text = await get_data(url)
    prepared_matrix = get_prepared_matrix(text)
    traversal_matrix = get_traversal_matrix(prepared_matrix)
    return traversal_matrix


def main():
    result = asyncio.run(get_matrix(SOURCE_URL))
    print(result)


if __name__ == '__main__':
    main()
