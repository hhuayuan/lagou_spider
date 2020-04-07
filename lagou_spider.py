# coding=utf-8

"""公众号：脾气暴躁的产品经理"""

import lxml
import time
from selenium import webdriver
from lxml import etree

browser = webdriver.Firefox()

for i in range(1, 31):
    print('page ', i)
    if i == 1:
        browser.get(
            'https://www.lagou.com/jobs/list_%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86?labelWords=&fromSearch=true&suginput=')
    else:
        browser.find_element_by_xpath('//span[@class="pager_next "]').click()
    html = browser.page_source
    # 把整个页面保存到本地备用
    f = open('%d.html' % i, 'w', encoding='utf-8')
    f.write(html)
    f.close()

    r = etree.HTML(html)
    li_lst = r.xpath("//li[contains(@class, 'con_list_item')]")
    print(len(li_lst))
    f = open('jd.txt', 'a', encoding='utf-8')
    for item in li_lst:
        titles = item.xpath('.//h3')
        areas = item.xpath('.//span[@class="add"]')
        pays = item.xpath('.//span[@class="money"]')
        industries = item.xpath('.//div[@class="industry"]')
        detail_url = item.xpath('.//a[@class="position_link"]/@href')[0]

        title = str(titles[0].text).replace(' ', '')
        lst = str(areas[0].xpath('string(.)')).replace('[', '').replace(']', '').split('·')
        if len(lst) > 0:
            city = lst[0]
        else:
            city = ''

        if len(lst) > 1:
            area = lst[1]
        else:
            area = ''

        lst = str(pays[0].text).replace('k', '').split('-')
        if len(lst) > 0:
            pay_low = lst[0]
        else:
            pay_low = ''

        if len(lst) > 1:
            pay_high = lst[1]
        else:
            pay_high = ''

        lst = str(industries[0].text).replace(' ', '').replace('\n', '').replace(',', '|').split('/')
        if len(lst) > 0:
            industry = lst[0]
        else:
            industry = ''

        if len(lst) > 1:
            finance = lst[1]
        else:
            finance = ''

        if len(lst) > 2:
            scale = lst[2]
        else:
            scale = ''

        # 职位, 城市, 区, 最低月薪, 最高月薪, 行业, 融资情况, 人员规模
        s = '%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (titles[0].text, city, area, pay_low, pay_high, industry, finance, scale, detail_url)
        f.write(s)
    f.close()
    time.sleep(8)
browser.quit()
print('ok')

