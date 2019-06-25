"""
Simple spider to demonstrate how to use the XLSX exporter.

This spider produces the following output:

+-----+----+---------+
|  a  | b  |    c    |
+=====+====+=========+
| foo | 42 | (empty) |
+-----+----+---------+
"""
from scrapy import Spider
from scrapy_xlsx import XlsxItemExporter

from ..items import ExampleItem


class CustomExporter(XlsxItemExporter):
    def __init__(self, file, **kwargs):
        super().__init__(file, default_value="(empty)", **kwargs)


class Example4Spider(Spider):
    name = "example4"
    allowed_domains = ["example.com"]
    start_urls = ["http://example.com/"]

    custom_settings = {
        "FEED_EXPORTERS": {"xlsx": "example.spiders.example4.CustomExporter"}
    }

    def parse(self, response):
        return ExampleItem(a="foo", b=42)
