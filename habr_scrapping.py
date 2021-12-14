import requests
import bs4
from pprint import pprint
import regex as re


KEYWORDS = {'developer', 'транспорт', 'web', 'python'}

headers_ = {'Cookie': '_ga=GA1.2.1061945960.1609002028; __gads=ID=26cc145ac1dc4142:T=1609001946:S=ALNI_MbL4B38x1WEXj1ixbuArRzSEQq_hw; _ym_uid=1609002030510094044; _ym_d=1631728739; fl=ru; hl=ru; cto_bundle=t6BQH196Q3hkYUt3SW1JZ0NONnA0bmQwNjNOMmRnMWdLem9XZXV6ODNyZmNPUTE2aHdaQ1ZRJTJCeE9uVWIwVVljWXhydEVYMURjVHdmbmdqOGxSeThBRTZtNXF3TCUyRk11NnNGY3MlMkJlb0lrZXBlQVBQbkolMkZvcjc2VXRIbVUlMkZOc2NxU3hzWUVnSFl1WGNpUmNQMzk3TCUyRjIzVjBwekElM0QlM0Q; feature_streaming_comments=true; _gid=GA1.2.1192023117.1639408687; habr_web_home=ARTICLES_LIST_ALL; _ym_isad=1; visited_articles=594705:595257:106414; _gat=1',
'Host': 'habr.com',
'If-None-Match': 'W/"36bad-lTQnTKt17oV7Ht3LI01VNUDP3XU"',
'Referer': 'https://github.com/netology-code/py-homeworks-advanced/tree/master/6.Web-scrapping',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36}'}


response = requests.get('https://habr.com/ru/all/', headers = headers_ )
response.raise_for_status()

text = response.text


soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    content = article.contents[0]
    title = content.h2.a.span.text
    dt = content.time['title']
    url = 'https://habr.com' + content.h2.a['href']
    preview = content.find('div', class_ = "tm-article-body").text
    set_title = set(re.split(r'\W+', title.lower() ))
    set_preview = set(re.split(r'\W+', preview.lower()))
    if KEYWORDS &  set_preview or KEYWORDS & set_title:
        print(title + '\n', dt + '\n', url)