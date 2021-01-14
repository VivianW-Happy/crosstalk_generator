# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import sys
# import pymysql
import re
import json


# --------set page amount----------

def set_download_urls():
    downloadUrls = []
    baseUrl = 'http://p.onegreen.net/JuBen/Search.asp?ModuleName=Article&Field=Title&Keyword=%C8%FD%BE%E4%B0%EB&ClassID=0&SpecialID=0&page='
    downloadUrls.append('http://p.onegreen.net/JuBen/Search.asp?ModuleName=Article&Field=Title&Keyword=%C8%FD%BE%E4%B0%EB&ClassID=0&SpecialID=0&page=1')
    # baseUrl = 'https://fanwen.chazidian.com/tag_%E4%B8%89%E5%8F%A5%E5%8D%8A/?page='
    # downloadUrls.append('https://fanwen.chazidian.com/tag_%E4%B8%89%E5%8F%A5%E5%8D%8A/?page=1')
    for i in range(2, 32):
        url = baseUrl + str(i)
        downloadUrls.append(url)
    return downloadUrls

##################################################
# # --------get download page urls
#
# def get_download_tables():
#     downloadUrls = set_download_urls()
#     tables = []
#     for url in downloadUrls:
#         req = requests.get(url)
#         req.encoding = 'utf-8'
#         html = req.text
#         table_bf = BeautifulSoup(html)
#         tables.append(table_bf.find('table', width=500, align='center'))
#
#     return tables
#
#
# # ---------get article links------------
# def get_download_url():
#     downloadTables = get_download_tables()
#     articles = []
#     for each in downloadTables:
#         articles.append(each.find_all('a', class_='link03'))
#     return articles
########################################################################

# ---------get article links------------
def get_download_url():
    downloadUrls = set_download_urls()
    articles = []
    for url in downloadUrls:
        req = requests.get(url)
        req.encoding = 'gb2312'
        # req.encoding = 'utf-8'
        html = req.text
        articles_bf = BeautifulSoup(html)
        articles.append(articles_bf.find_all('a',class_='LinkSearchResult'))
        # articles.append(articles_bf.find_all('div', class_='listpage-item'))
    return articles


def read_article_info():
    articles = get_download_url()
    baseUrl = 'http://p.onegreen.net/'
    # baseUrl = 'https://fanwen.chazidian.com/'
    dict = {}
    i=0
    for each in articles:
        for item in each:
            # item=item.find('h4').find('a')  #后加的
            dict[i] = baseUrl + item.get('href')[1:]
            i=i+1
    return dict
# def read_article_info():
#     # articles = get_download_url()
#     baseUrl = 'http://www.17989.com/sanjubantaici/'
#     # 'http://p.onegreen.net/'
#     # baseUrl = 'https://fanwen.chazidian.com/'
#     dict = {}
#
#     for i in range(1,110):
#         dict[i] = baseUrl + str(i) + '.htm'
#
#     return dict



def get_content(title, url):
    print(str(title) + '---->' + url)
    req = requests.get(url)
    req.encoding = 'gb2312'
    # req.encoding = 'utf-8'
    html = req.text
    text_bf = BeautifulSoup(html)

    # article = text_bf.find('div',class_='article-text')
    # text = ""
    # article = text_bf.find('div', class_='module articlelist')
    # content = article.select("p")
    # for item in content:
    #     text += item.get_text()
    #     text += "\n"



############################################################
    text = ""
    article = text_bf.find('div', id = 'main2')
    content = article.get_text()
    text = content
######################################################
    # content = article.select("p")
    # text = ""
    # for item in content:
    #     text += item.get_text()
    #     text += "\n"

    # ----article content-----
    # content = article.find(class_='TRS_Editor').get_text()
    # content = article.find('div',attrs={'id':re.compile("TRS_")}).select("p")
    # content = article.select("p")
    # info = article.find(class_='hui_12-12').get_text()
    # date = info[3:19]
    # source = info.split("：")[3]

    ###############################################
    # content = article.get_text()
    # text = ""
    # text+=content
    ###############################################

    # index=content.find("（载入中...）")
    # lenth1=len("（载入中...）")
    # lenth2 = len(content)
    # text+=content[index+lenth1+1:lenth2]

    # for item in content:
    #     text += item.get_text()
    #     text += "\n"

    # print(text)

    write_item_to_file(text)

###########################



def write_item_to_file(item):
    print('开始写入数据 ====> ' + str(item))
    with open('sanjuban_11111.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
# --------save all article -----------

def save_data():
    dict = read_article_info()
    for key, value in dict.items():
        get_content(key, value)

save_data()