import datetime

from bs4 import BeautifulSoup


def get_max_date(src_date, months):
    months += 1
    month = src_date.month - 1 + months
    year = src_date.year + month // 12
    month = month % 12 + 1
    return datetime.date(year, month, 1)


def create_soup(text):
    return BeautifulSoup(text, 'html.parser')
