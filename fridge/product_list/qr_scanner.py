from pyzbar import pyzbar
import re
import requests
from collections import namedtuple


HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}

URL = 'https://consumer.1-ofd.ru/api/tickets/ticket/'

# В аргументы принимает кортеж из именованных кортежей decode функции. Возвращает список из json-чеков
def parse_data(raw_data: tuple) -> list:
    global URL
    qr_list = list()
    for check in raw_data:
        URL += f'?t={check.t}&s={check.s}&fn={check.fn}&i={check.i}&fp={check.fp}&n={check.n}'
        data = requests.get(url=URL).json()
        qr_list.append(data)
    return qr_list

def parse_data_1(fn, i, fp):
    URL = f'https://check.ofd.ru/rec/{fn}/{i}/{fp}'
    data = requests.get(URL)
    return data.text

# Написал скан и преобразование в удобный формат. Регулярку и формат чека нужно будет много раз протестить
def decode(*args) -> tuple:
    qr_list = tuple(qr.data for qr in pyzbar.decode(*args))
    QR = namedtuple('QR', ('t', 's', 'fn', 'i', 'fp', 'n'))
    return tuple(QR(*re.findall(r"(?<==)[0-9.A-Z]+", str(qr))[:6]) for qr in qr_list)



