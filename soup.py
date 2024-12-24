from bs4 import BeautifulSoup


if __name__ == '__main__':
    simple_html = '<html><body><p>Это самый простой HTML!</p></body></html>'
    soup = BeautifulSoup(simple_html, features='html.parser')

    tag_p = soup.p
    print(tag_p)
