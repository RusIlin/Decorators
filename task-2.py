import datetime as dt
import os
import requests

PATH_DIR = os.getcwd()


def logger(path):
    def decor(func):
        def foo(*args, **kwargs):
            date_time = dt.datetime.now()
            name = func.__name__
            result = func(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as f:
                f.write(f'Дата и время: {date_time:%b.%d %H:%M}\n'
                        f'Имя функции: {name}\n'
                        f'Аргументы: {args, kwargs}\n'
                        f'Возвращаемое значение: {result}\n')
            return result

        return foo

    return decor


@logger(f"{os.path.abspath(os.path.join(PATH_DIR, 'decor.txt'))}")
def get_status(*args):
    url = ','.join(args)
    response = requests.get(url=url)
    return response.status_code


if __name__ == '__main__':
    get_status('https://yandex.ru/')
