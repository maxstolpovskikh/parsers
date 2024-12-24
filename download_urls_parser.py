import re
from pathlib import Path
from urllib.parse import urljoin

import requests_cache
from bs4 import BeautifulSoup
from tqdm import tqdm

DOWNLOADS_URL = 'https://docs.python.org/3/download.html'
BASE_DIR = Path(__file__).parent


if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(DOWNLOADS_URL)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, features='lxml')

    table_tag = soup.find('table', class_='docutils')

    pdf_a4_tag = table_tag.find('a', {'href': re.compile(r'.+pdf-a4\.zip$')})

    pdf_a4_link = pdf_a4_tag['href']

    archive_url = urljoin(DOWNLOADS_URL, pdf_a4_link)

    filename = archive_url.split('/')[-1]

    print(filename)

    downloads_dir = BASE_DIR / 'downloads'

    downloads_dir.mkdir(exist_ok=True)

    archive_path = downloads_dir / filename

    response = session.get(archive_url)

    with open(archive_path, 'wb') as file:
        file.write(response.content)
