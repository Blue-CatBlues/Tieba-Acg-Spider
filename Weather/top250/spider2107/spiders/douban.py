import scrapy
from scrapy import Selector, Request
from spider2107.items import MovieItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ["https://movie.douban.com/top250?start=0&filter="]

    # 模拟浏览器请求,并且爬取下一页要保持请求头
    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers)

    def parse(self, response):
        sel = Selector(response)
        list_items = sel.css("#content > div > div.article > ol > li")
        print(f"Found {len(list_items)} items")
        for list_item in list_items:
            movie_item = MovieItem()
            movie_item["title"] = list_item.css("span.title::text").extract_first()
            movie_item["rank"] = list_item.css("span.rating_num::text").extract_first()
            movie_item["subject"] = list_item.css("span.inq::text").extract_first()
            print(movie_item)
            yield movie_item

        # 找到“下一页”链接
        next_page = sel.css("div.paginator > span.next > a::attr(href)").extract_first()
        if next_page:
            next_page_url = response.urljoin(next_page)
            print(f"Next page URL: {next_page_url}")  # 调试信息
            yield Request(url=next_page_url, headers=response.request.headers, callback=self.parse)
