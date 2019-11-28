import asyncio
import os

import aiohttp
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from tqdm import tqdm

def crawl(url):
    links = fetch_links(url)
    loop = asyncio.get_event_loop()
    responses = loop.run_until_complete(download(links))
    loop.close()
    return responses

def fetch_links(url):
    links = []
    base_url = os.path.dirname(url)
    manual = requests.get(url)
    if manual.status_code == 200:
        manual = BeautifulSoup(manual.text, 'lxml')
        for anchor in manual.find_all('a', href=True):
            if 'man1' in anchor['href']:
                links.append(f'{base_url}/{anchor["href"]}')
    else:
        raise ValueError(f'{url} did not respond')

    return links

async def download(links):
    tasks = []
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=100)) as client:
        for link in links:
            task = asyncio.ensure_future(fetch(client, link))
            tasks.append(task)

        responses = [await r for r in tqdm(asyncio.as_completed(tasks), total=len(tasks)) if r is not None]

    return responses

async def fetch(client, link):
    async with client.get(link) as r:
        if r.status == 200:
            response = await r.text()
            return await serialize(link, response)


async def serialize(link, page):
    entry = dict(link=link)
    page = BeautifulSoup(page, 'lxml')
    sections = page.find('p', attrs={'class':'section-dir'})
    if sections is not None:
        for section in sections.find_all('a', href=True):
            section_name = section.text.lower()
            html_section = page.find('a', attrs={'id': section.text})
            if html_section is not None:
                entry[section_name] = html_section.findNext('pre').text

    return entry


if __name__ == '__main__':
    manpages = crawl('http://man7.org/linux/man-pages/dir_section_1.html')

    client = MongoClient('localhost', 27017)
    db = client.test_database
    db.manpages.insert_many(manpages)
