from setuptools import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='scrapy-xlsx',
    version='0.1.0',
    description='XLSX exporter for Scrapy',
    long_description=readme,
    author='Jesús Losada Novo',
    author_email='dev@jesuslosada.com',
    url='https://github.com/jesuslosada/scrapy-xlsx',
    license='MIT',
    packages=['scrapy_xlsx'],
    install_requires=['scrapy', 'openpyxl'],
    tests_require=['tox', 'pytest'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries'
    ],
    keywords=['scrapy', 'xlsx', 'exporter']
)
