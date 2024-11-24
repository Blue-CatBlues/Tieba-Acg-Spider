import scrapy
from scrapy import Selector
from spider2024.items import actor_link
import json

class ActorSpider(scrapy.Spider):
    name = 'KB'
    allowed_domains = ['baike.baidu.com']
    start_urls = [
        'https://baike.baidu.com/item/%E7%8B%82%E9%A3%99/57027307']

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
        }
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers)

    def parse(self, response):
        self.log(f"Response status: {response.status}")
        self.log(f"Response body: {response.text[:600]}")

        sel = Selector(response)
        list_items = sel.css("#J-lemma-main-wrapper > div.contentWrapper_vLuvc > div > div.mainContent_jQUQT > div > div.J-lemma-content > div:nth-child(9) > div > div > div > div > div > div ")
        self.log(f"找到了 {len(list_items)} items")

        items = []
        for list_item in list_items:
            actor_item = actor_link()
            actor_item["name"] = list_item.css("a::text").get()
            print(actor_item["name"])
            actor_item["link"] = response.urljoin(list_item.css("a::attr(href)").get())
            print(actor_item["link"])
            # 只将 name 不为 null 的项添加到 items 列表中
            if actor_item["name"] is not None:
                items.append(dict(actor_item))

        # 将数据写入 JSON 文件，确保以 UTF-8 编码保存
        with open('D:\\AAAPycharmProjects\\KB\\actors_link.json', 'w', encoding='utf-8') as f:
            json.dump(items, f, ensure_ascii=False, indent=4)  # 使用 ensure_ascii=False
        self.log("数据已写入 Actor_link.json 文件")