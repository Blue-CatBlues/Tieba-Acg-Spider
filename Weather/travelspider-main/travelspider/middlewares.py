# 在这里定义你的爬虫中间件模型
#
# 参见文档：
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# 便于处理不同类型的项目
from itemadapter import is_item, ItemAdapter


class TravelspiderSpiderMiddleware:
    # 并非所有方法都需要定义。如果某个方法未定义，
    # Scrapy将视为爬虫中间件不修改传递的对象。

    @classmethod
    def from_crawler(cls, crawler):
        # 此方法用于Scrapy创建你的爬虫。
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # 对每个通过爬虫中间件的响应调用此方法。

        # 应返回None或引发异常。
        return None

    def process_spider_output(self, response, result, spider):
        # 在爬虫处理响应后，调用此方法以返回结果。

        # 必须返回一个可迭代的请求或项目对象。
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # 当爬虫或process_spider_input()方法
        # （来自其他爬虫中间件）引发异常时调用。

        # 应返回None或可迭代的请求或项目对象。
        pass

    def process_start_requests(self, start_requests, spider):
        # 用于爬虫的起始请求，工作方式类似于process_spider_output()方法，
        # 只不过没有关联的响应。

        # 必须仅返回请求（而不是项目）。
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("爬虫已开启: %s" % spider.name)


class TravelspiderDownloaderMiddleware:
    # 并非所有方法都需要定义。如果某个方法未定义，
    # Scrapy将视为下载器中间件不修改传递的对象。

    @classmethod
    def from_crawler(cls, crawler):
        # 此方法用于Scrapy创建你的爬虫。
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # 对每个通过下载器中间件的请求调用此方法。

        # 必须：
        # - 返回None：继续处理此请求
        # - 或返回一个Response对象
        # - 或返回一个Request对象
        # - 或引发IgnoreRequest：调用已安装下载器中间件的process_exception()方法
        return None

    def process_response(self, request, response, spider):
        # 当下载器返回响应时调用此方法。

        # 必须：
        # - 返回一个Response对象
        # - 返回一个Request对象
        # - 或引发IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # 当下载处理程序或process_request()
        # （来自其他下载器中间件）引发异常时调用。

        # 必须：
        # - 返回None：继续处理此异常
        # - 返回一个Response对象：停止process_exception()链
        # - 返回一个Request对象：停止process_exception()链
        pass

    def spider_opened(self, spider):
        spider.logger.info("爬虫已开启: %s" % spider.name)
