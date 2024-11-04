import scrapy
from scrapy import Selector
from spider2024.items import TiebaItem

class AcgSpider(scrapy.Spider):
    name = 'acg'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f/index/forumpark?cn=&ci=0&pcn=%E5%8A%A8%E6%BC%AB%E5%AE%85&pci=206&ct=&st=new&pn=1']

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        for page in range(1, 31):  # 循环生成1到30页的URL
            url = f'https://tieba.baidu.com/f/index/forumpark?cn=&ci=0&pcn=%E5%8A%A8%E6%BC%AB%E5%AE%85&pci=206&ct=&st=new&pn={page}'
            yield scrapy.Request(url, headers=headers)

    def parse(self, response):
        sel = Selector(response)
        list_items = sel.css("#ba_list > div")
        print(f"Found {len(list_items)} items")
        for list_item in list_items:
            tieba_item = TiebaItem()
            tieba_item["name"] = list_item.css("a > div > p.ba_name::text").extract_first()
            tieba_item["member"] = list_item.css("a > div > p.ba_num.clearfix > span.ba_m_num::text").extract_first()
            tieba_item["comment"] = list_item.css("a > div > p.ba_num.clearfix > span.ba_p_num::text").extract_first()
            tieba_item["main"] = list_item.css("a > div > p.ba_desc::text").extract_first()
            print("能够抓取到：" + str(tieba_item))
            yield tieba_item
