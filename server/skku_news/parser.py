import re
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

def get_object(link):
    html = urlopen(link)
    bs_object = bs(html, "html.parser")
    return bs_object

def main_crawling(page: bs):
    articles = page.select("dl.board-list-content-wrap")

    results = []
    for article in articles:
        title_element = article.select_one("dt > a")
        title = title_element.string.strip()
        link = title_element.get('href')
        title_element['href']

        info_elements = article.select("dd > ul > li")
        number = re.sub(r'[^0-9]', '', info_elements[0].string.strip())
        date = info_elements[2].string.strip()
        results.append({
            "num": number,
            "title": title.replace("'", "''"),
            "date": date,
            "link": link
        })
    return results

if __name__ == "__main__":
    page = get_object("https://www.skku.edu/skku/campus/skk_comm/notice01.do")
    main_crawling(page)
