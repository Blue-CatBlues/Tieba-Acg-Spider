import openpyxl

class ExcelPipeline:
    def open_spider(self, spider):
        # 当爬虫开启时调用此方法，创建一个新的 Excel 工作簿
        self.wb = openpyxl.Workbook()
        self.sheet = self.wb.active
        self.sheet.append(['电影', '评分', '主题'])
        spider.logger.info("Excel 文件已创建")

    def close_spider(self, spider):
        self.wb.save('top250_output.xlsx')  # 尝试不同的文件名
        spider.logger.info("Excel 文件已保存")

    def process_item(self, item, spider):
        spider.logger.info(f"处理项目: {item['title']}, {item['rank']}, {item['subject']}")
        self.sheet.append([item['title'], item['rank'], item['subject']])
        return item