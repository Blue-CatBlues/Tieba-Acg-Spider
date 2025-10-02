# Tieba ACG Spider 🕷️
一个用于爬取百度贴吧「动漫宅」分区的 Scrapy 爬虫，自动提取每个吧的名称、关注人数、帖子数和简介，并输出为 Excel 文件。支持数据排序分析，快速洞察贴吧热度分布。

---

## 🚀 功能亮点

- ✅ 自动爬取 30 页 ACG 分区贴吧信息
- ✅ 提取吧名、关注人数、帖子数、简介等字段
- ✅ 输出为 Excel 文件，便于后续分析
- ✅ 使用 pandas 进行排序分析，展示前/后 20 个贴吧的热度对比

---

## 🛠️ 使用方法

### 1️⃣ 安装依赖

```bash
conda create -n tieba_spider python=3.10
conda activate tieba_spider
pip install scrapy pandas openpyxl
```
### 2️⃣ 运行爬虫
```bash
scrapy crawl acg
输出结果将保存在 acg_output.xlsx
```
### 3️⃣ 分析数据
- 可以直接在ide里点击运行文件，也可以在命令行使用指令操作
```bash
python analyse/acg_analyse.py
python analyse/stu.py
# 可视化分析脚本
python analyse/picture.py
python analyse/picture2.py
python analyse/picture3.py
