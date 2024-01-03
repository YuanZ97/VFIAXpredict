import requests
from bs4 import BeautifulSoup
import time
from backend import local_user_agent
from .models import PriceEntry, StockEntry, DateEntry

def get_stock_data(user_agent, url, stock):
    header = {'User-Agent': user_agent}
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    calendar = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
    response = requests.get(url, headers = header)
    soup = BeautifulSoup(response.content, 'html5lib')
    spans = soup.find_all('span')

    for i in range(len(spans) - 5):
        for j in range(len(month)):
            # ensure that there is no range for the data (clean the data)
            if "-" in spans[i].text:
                continue

            if month[j] in spans[i].text:
                # check if the data already exists in the db
                if DateEntry.objects.filter(date = rearrage_date(spans[i].text, calendar)).exists():
                    break
          
                date_object = DateEntry.objects.create(date = rearrage_date(spans[i].text, calendar))
                stock_object = StockEntry.objects.create(type = stock, date = date_object)
                price_object = PriceEntry.objects.create(open = spans[i + 1].text, high = spans[i + 2].text, low = spans[i + 3].text, close = spans[i + 4].text, adj_close = spans[i + 5].text, stock = stock_object)


def repeat_scrapping_VFIAX(seconds):
    user_agent = local_user_agent.id
    url = 'https://finance.yahoo.com/quote/VFIAX/history'
    stock = 'VFIAX'

    while True:
        new_data= get_stock_data(user_agent, url, stock)
        time.sleep(seconds)


def rearrage_date(date, calendar):
    date = date.replace(',', '')
    date = date.split()
    date = date[2] + '-' + calendar[date[0]] + '-' + date[1]
    return str(date)