import scrapy
from bs4 import BeautifulSoup
from travelspider.items import TravelspiderItem


class TravelSpider(scrapy.Spider):
    name = "travel"
    allowed_domains = ["travel.qunar.com"]
    start_urls = [
         f"https://travel.qunar.com/p-cs299979-chongqing-jingdian"

         # ,*[f"https://travel.qunar.com/p-cs299979-chongqing-jingdian-1-{page}" for page in range(2, 200)]
    ]

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)
        # 提取景点信息
        items = soup.find_all('div', class_='item')
        for item in items:
            name = item.find('span', class_='cn_tit').get_text(strip=True)
            review_count = item.find('span', class_='icon_comment').next_sibling.strip()
            rating_percentage = int(item.find('span', class_='cur_star')['style'].split(':')[1].strip('%;'))

            travel_item = TravelspiderItem()
            travel_item['name'] = name
            travel_item['review_count'] = review_count
            travel_item['score'] = rating_percentage

            yield travel_item

