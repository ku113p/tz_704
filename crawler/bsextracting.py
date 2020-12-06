import datetime

from bs4 import BeautifulSoup

from config import max_date


def event_info(inner_soup: BeautifulSoup, href):
    desc = inner_soup.find('div', {'class': 'event-description'})

    return {
        'href': href,
        'title': inner_soup.find('h1', {'class': 'single-event-title'}).get_text().strip(),
        'location': inner_soup.find('span', {'class': 'single-event-location'}).get_text().strip() or None,
        'date': {
            'start': dates.find('time', {'class': ['date-start', 'time-start']})['datetime'],
            'end': dates.find('time', {'class': ['date-end', 'time-end']})['datetime'],
        } if (dates := inner_soup.find('h3', {'class': 'single-event-date'})) else None,
        'desc': {
            'text': a.get_text().strip(),
            'link': a['href']
        } if (a := desc.find('a')) else {'text': desc.get_text().strip()}
    }


def events_inner_links(main_soup: BeautifulSoup):
    if not (events := main_soup.select('div.event-widget.last')):
        return

    for li in events[0].find_all('li'):
        if datetime.datetime.fromisoformat(li.find('time')['datetime']).date() < max_date:
            yield li.find('a')['href']
