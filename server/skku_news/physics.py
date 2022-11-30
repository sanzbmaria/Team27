import json
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

def get_object(link):
    html = urlopen(link)
    bs_object = bs(html, "html.parser")
    return bs_object

def main_crawling(page: bs):
    articles = page.select("dl.board-list-content-wrap")

    for article in articles:
        title_element = article.select_one("dt > a")
        title = title_element.string.strip()
        link = title_element.get('href')
        title_element['href']

        info_elements = article.select("dd > ul > li")
        number = info_elements[0].string.strip()
        date = info_elements[2].string.strip()
        print(title)
        print(link)

        print(number)
        print(date)
        file = open("physics", "w")
        output = {
          "num":number,
          "title":title,
          "date":date,
          "link":link
          }
        json.dump(output, file)
        file.close()

if __name__ == "__main__":
    page = get_object("https://skb.skku.edu/physics/notice/notice.do")
    main_crawling(page)


