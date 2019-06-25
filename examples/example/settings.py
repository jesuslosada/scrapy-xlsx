BOT_NAME = "example"

SPIDER_MODULES = ["example.spiders"]
NEWSPIDER_MODULE = "example.spiders"

FEED_EXPORTERS = {"xlsx": "scrapy_xlsx.XlsxItemExporter"}
