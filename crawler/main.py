import json
import sys
from urllib.parse import urljoin

import aiohttp
import asyncio

from bsextracting import event_info, events_inner_links
from config import src_url, pause_between_requests
from utils import create_soup


async def get_links(session: aiohttp.ClientSession):
    async with session.get(src_url) as rsp:
        soup = create_soup((await rsp.read()).decode('utf-8'))
        for href in events_inner_links(soup):
            yield href


async def event_inner_soup(session: aiohttp.ClientSession, href):
    async with session.get(urljoin(src_url, href)) as rsp:
        return create_soup((await rsp.read()).decode('utf-8'))


async def main():
    async with aiohttp.ClientSession() as session:
        async for href in get_links(session):
            event_soup = await event_inner_soup(session, href)
            data = event_info(event_soup, href)
            sys.stdout.write(f'{json.dumps(data)}\n')
            await asyncio.sleep(pause_between_requests)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
