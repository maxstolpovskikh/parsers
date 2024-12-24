import re

import requests_cache
from bs4 import BeautifulSoup


MAIN_DOC_URL = 'https://docs.python.org/3/'


if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(MAIN_DOC_URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='lxml')

    side_bar = soup.find('div', class_='sphinxsidebarwrapper')
    ul_tags = side_bar.find_all('ul')

    for ul in ul_tags:
        if 'All versions' in ul.text:
            a_tags = ul.find_all('a')
            break
    else:
        raise Exception('Ничего не нашлось')

    results = []
    pattern = r'Python (?P<version>\d\.\d+) \((?P<status>.*)\)'

    for a_tag in a_tags:
        version = text = a_tag.text
        if re.match(pattern, text):
            text_match = re.search(pattern, text)
            version, status = text_match.groups()
        results.append((a_tag['href'], version, status))

    for row in results:
        print(*row)
