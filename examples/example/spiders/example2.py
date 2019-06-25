"""
Simple spider to demonstrate the XLSX exporter.

This spider produces the following output:

+-----+----+-----+
| foo | 42 | bar |
+-----+----+-----+
"""
from scrapy import Spider
from scrapy_xlsx import XlsxItemExporter

from ..items import ExampleItem


class CustomExporter(XlsxItemExporter):
    def __init__(self, file, **kwargs):
        super().__init__(file, include_header_row=False, **kwargs)


class Example2Spider(Spider):
    name = "example2"
    allowed_domains = ["example.com"]
    start_urls = ["http://example.com/"]

    custom_settings = {
        "FEED_EXPORTERS": {"xlsx": "example.spiders.example2.CustomExporter"}
    }

    def parse(self, response):
        return ExampleItem(a="foo", b=42, c="bar")
