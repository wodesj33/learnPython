#!/usr/bin/python3

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pyquery import PyQuery as pq
import time

browser = webdriver.Chrome()

browser.get("http://deal.ggzy.gov.cn/ds/deal/dealList.jsp")

i = 1
while i <= 94039:  # 94039
    try:
        browser.find_element_by_id('PAGENUMBER')
    except NoSuchElementException:
        browser.get("http://deal.ggzy.gov.cn/ds/deal/dealList.jsp")

    # document.getElementById("PAGENUMBER").value = 10;
    url = 'document.getElementById("PAGENUMBER").value=' + str(i)
    browser.execute_script(url)

    try:
        browser.execute_script('document.getElementById("FIND").submit();')
    except TimeoutException:
        continue

    html = pq(browser.page_source)
    html2 = pq(str(html('.publicont')))

    length = html2('a').length

    j = 0
    while j < length:
        href = html2('a').eq(j).attr('href')
        title = html2('a').eq(j).html()
        print(href, title)
        j = j + 1

    i = i + 1
    # time.sleep(1)

# browser.close()
