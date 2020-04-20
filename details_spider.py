# coding=utf-8

"""公众号：脾气暴躁的产品经理"""

import lxml
import time
import os
from selenium import webdriver
from lxml import etree

def get_html():
    browser = webdriver.Firefox()
    f = open('jd.txt', 'r', encoding='utf-8')
    lst = f.readlines()
    f.close()

    for item in lst:
        url = item.split(',')[-1].replace('\n', '')
        print(url)
        file_name = url.split('/')[-1].split('.')[0]

        browser.get(url)

        html = browser.page_source
        # 把整个页面保存到本地备用
        f = open('./details/%s.html' % file_name, 'w', encoding='utf-8')
        f.write(html)
        f.close()
        time.sleep(2)
    browser.quit()


def parse_html():
    f_details = open('details.txt', 'a', encoding='utf-8')
    for (root, dirs, files) in os.walk('./details'):
        for f in files:
            file_name = os.path.join(root, f)
            print(file_name)

            f = open(file_name, 'r', encoding='utf-8')
            html = f.read()
            f.close()

            r = etree.HTML(html)
            job_advantage = r.xpath('//dd[@class="job-advantage"]')[0]
            f_details.write(job_advantage.xpath('string(.)'))
            job_bt = r.xpath('//dd[@class="job_bt"]')[0]
            f_details.write(job_bt.xpath('string(.)'))


if __name__ == '__main__':
    get_html()
    parse_html()
    print('ok')

