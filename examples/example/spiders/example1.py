"""
Simple spider to demonstrate how to use the XLSX exporter.

This spider produces the following output:

+-----+----+---+
|  a  | b  | c |
+=====+====+===+
| foo | 42 |   |
+-----+----+---+
"""
from scrapy import Spider

from ..items import ExampleItem


class Example1Spider(Spider):
    name = "example1"
    allowed_domains = ["example.com"]
    start_urls = ["http://example.com/"]

    def parse(self, response):
        return ExampleItem(a="foo", b=42)
