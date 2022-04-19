import os

import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def Web_scraping():

    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    from selenium.webdriver.common.by import By
    driver.get('https://www.giiresearch.com/material_report.shtml')
    title_list = driver.find_elements(By.XPATH, '//div[@class="list_title"]')
    published_by_list = driver.find_elements(By.XPATH, '//div[@class="plist_pubinfo"]//div[@class="plist_info_dd2"]')
    product_code_list = driver.find_elements(By.XPATH, '//div[@class="plist_codeinfo"]//div[@class="plist_info_dd2"]')
    published_list = driver.find_elements(By.XPATH, '//div[@class="plist_dateinfo"]//div[@class="plist_info_dd2"]')
    page_info_list = driver.find_elements(By.XPATH, '//div[@class="plist_pageinfo"]//div[@class="plist_info_dd2"]')
    # priceInfoList = driver.find_elements(By.XPATH,
    #                                      '//div[@class="plist_priceinfo"]//div[@class="plist_info_dd2"]//span[@class="price_usd"]')

    title = []
    for i in range(len(title_list)):
        title.append(title_list[i].text)

    published_by = []
    for i in range(len(published_by_list)):
        published_by.append(published_by_list[i].text)

    product_code = []
    for i in range(len(product_code_list)):
        product_code.append(product_code_list[i].text)

    published = []
    for i in range(len(published_list)):
        published.append(published_list[i].text)

    page_info = []
    for i in range(len(page_info_list)):
        page_info.append(page_info_list[i].text)
    #
    # priceInfo = []
    # for i in range(len(priceInfoList)):
    #     priceInfo.append(priceInfoList[i].text)



    data = pd.DataFrame()
    data['Title']= title
    data['Published By'] = published_by
    # data['Price Info'] = priceInfo
    data['Page Info'] = page_info
    data['Published'] = published
    data['Product Code'] = product_code
    data["Published"] = pd.to_datetime(data["Published"])
    start_date = "April 14, 2022"
    end_date = "April 18, 2022"
    start_day = pd.to_datetime(start_date)
    end_day = pd.to_datetime(end_date)
    data[data['Published'].dt.date.between(start_day.date(), end_day.date())].to_csv(os.getcwd() + '\\output.csv',
                                                                                     index=False)


if __name__ == '__main__':
    Web_scraping()