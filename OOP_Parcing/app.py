from parsers.cars import Cars
from parsers.work import Work
from parsers.news import News

news_url = "https://www.kaubamaja.ee/meist/kulasta-meid-kaubamajas/kontakt"
work_url = 'https://istrek.com/ru/%d0%be-%d1%84%d0%b8%d1%80%d0%bc%d0%b5/'
cars_url = "https://rus.auto24.ee/"

# work for example
with Work(work_url) as work:
    for el in work.parse():
        work.display_item(el)
