===========
scrapy-xlsx
===========

**scrapy-xlsx** is a `Scrapy`_ exporter that supports the XLSX format. It
produces files that can be read with Microsoft Excel or LibreOffice Calc.

Usage
-----

Install the library using `pip`_::

    $ pip install scrapy_xlsx

Configure the exporter in your Scrapy project ``settings.py`` file::

    FEED_EXPORTERS = {
        'xlsx': 'scrapy_xlsx.XlsxItemExporter',
    }

Run your spider and export the data to XLSX (this command will overwrite the
output file if it already exists)::

    $ scrapy crawl myspider -o output.xlsx

License
-------

Licensed under the MIT License.

.. _Scrapy: https://scrapy.org/
.. _pip: https://pypi.org/project/pip/