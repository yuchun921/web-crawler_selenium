import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# 使用 selenium 將瀏覽器自動開啟取得網頁資訊後關閉
try:
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")
    # 建立chrome物件，用抓取的driver路徑進行初始化
    chrome = webdriver.Chrome(options=option,
        executable_path="C:\\Users\\yuchun\\Desktop\\Python100D\\Codegym\\selenium\\chromedriver.exe")
    # 因為這次不是使用request，因此無法得知網頁回傳狀態使否為 200，所以用timeout等待網頁回應
    chrome.set_page_load_timeout(10)
    chrome.get("https://code-gym.github.io/spider_demo/")
    # bs4解析網頁資訊
    # chrome.page_source 是chrome的物件屬性，會回傳網頁內容
    soup = BeautifulSoup(chrome.page_source, "html5lib")
    # 搜尋標籤h1的資料
    print(soup.find("h1").text)

    chrome.find_element_by_xpath(
        "/html/body/div[2]/div/div[1]/div[1]/div/div/h3/a").click()
    print(chrome.find_element_by_xpath("//*[@id='post-header']/div[2]/div/div/h1").text)
finally:
    # 關閉瀏覽器
    chrome.quit()
