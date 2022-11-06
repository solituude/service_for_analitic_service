import requests
import codecs
from bs4 import BeautifulSoup as BS

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/2010001 Firefox/47.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

domain = 'https:'
url = 'https://sob.ru/prodazha-kvartir-moskva'
resp = requests.get(url, headers=header)
ads = []
if resp.status_code == 200:
    soup = BS(resp.content, 'html.parser')
    main_div = soup.find('div', attrs={'class': 'grid-search-content'})
    div_lst = main_div.find_all('div', attrs={'class': 'adv-card'})
    for div in div_lst:
        title = div.find('div', attrs={"class": "adv-card-title"})
        href = title.a['href']
        price = div.find('div', attrs={'class': 'adv-card-price'})  # цена
        info = div.find('div', attrs={'class': 'adv-card-info'})  # вся краткая информация
        to_metro = div.find('span')  # сколько минут до метро
        address = div.find('div', attrs={'class': 'b-adAddress'})  # плохо записанный адрес
        print(to_metro.text)


h = codecs.open('sob.html', 'w', 'utf-8')
h.write(str(resp.text))
h.close()

