import requests
from bs4 import BeautifulSoup
import time
import local_user_agent

def get_stock_data(user_agent, url):
  header = {'User-Agent': user_agent}
  month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  db = {}

  response = requests.get(url, headers = header)
  soup = BeautifulSoup(response.content, 'html5lib')
  spans = soup.find_all('span')

  for i in range(len(spans) - 5):
    for j in range(len(month)):

      if "-" in spans[i].text:
        continue

      if month[j] in spans[i].text:
        date = spans[i].text
        open_price = spans[i + 1].text
        high_price = spans[i + 2].text
        low_price = spans[i + 3].text
        close_price = spans[i + 4].text
        adj_close = spans[i + 5].text
        db[date] = [open_price, high_price, low_price, close_price, adj_close]

  return db


def repeat_scrapping(seconds):
  user_agent = local_user_agent.id
  url = 'https://finance.yahoo.com/quote/VFIAX/history'
  while True:
    test = get_stock_data(user_agent, url)
    print(test)
    print('------------')
    time.sleep(seconds)