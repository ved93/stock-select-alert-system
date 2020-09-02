# import feedparser
# import pathlib
# import re

# root = pathlib.Path(__file__).parent.resolve()

# print(root)


# def replace_chunk(content, marker, chunk, inline=False):
#     r = re.compile(
#         r'<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->'.format(marker, marker),
#         re.DOTALL,
#     )
#     if not inline:
#         chunk = '\n{}\n'.format(chunk)
#     chunk = '<!-- {} starts -->{}<!-- {} ends -->'.format(marker, chunk, marker)
#     return r.sub(chunk, content)


# def fetch_writing():
#     entries = feedparser.parse('https://d4datascience.wordpress.com/feed')['entries'][:5]
#     return [
#         {
#             'title': entry['title'],
#             'url': entry['link'].split('#')[0],
#             'published': re.findall(r'(.*?)\s00:00', entry['published'])[0]
#         }
#         for entry in entries
#     ]


# if __name__ == '__main__':
#     readme_path = root / 'README.md'
#     readme = readme_path.open().read()
#     # entries = fetch_writing()[:5]
#     # entries_md = '\n'.join(
#     #     ['* [{title}]({url}) - {published}'.format(**entry) for entry in entries]
#     # )
#     # rewritten = replace_chunk(readme, 'writing', entries_md)

#     # readme_path.open('w').write(rewritten)


# Import libraries
import requests
from bs4 import BeautifulSoup
import requests_html
import lxml.html as lh
import pandas as pd
import re
# from datetime import datetime
# from datetime import timedelta
# import mysql.connector as sql
# import DBcm
# import time
# import unidecode #used to convert accented words


# df = pd.read_csv('tickers.csv')

stocks_list = ['CRISIL.NS','GODREJCP.NS','MARICO.NS','HDFCBANK.NS', 'INDUSINDBK.NS']

for stock in stocks_list:
    url = 'https://query1.finance.yahoo.com/v8/finance/chart/{}?region=IN&lang=en-IN&includePrePost=false&interval=2m&range=1d&corsDomain=in.finance.yahoo.com&.tsrc=finance'.format(stock)
    
    session = requests_html.HTMLSession()
    r = session.get(url)

    content=BeautifulSoup(r.content, 'lxml')
    # content
    print(str(content).split('regularMarketPrice')[1].split('chartPreviousClose')[0][2:-2])
    
    