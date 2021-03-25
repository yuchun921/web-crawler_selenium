# Selenium

Selenium可以將瀏覽器作業流程自動化，模擬使用者操作瀏覽器的行為，常用於測試web application居多，但也可以用於爬蟲。

### 下載selenium driver
使用之前要先安裝與瀏覽器相配的driver<br>
(google的話:要先看版本，可以在[關於Google Chrome]中查到)<br>
(記得解壓縮後的檔案路徑，程式中會用的到)<br>
http://chromedriver.chromium.org/downloads<br>

### 安裝 selenium
在python中安裝**pip install selenium**


## 實作說明
1. 使用selenium抓取主機回傳的html給beautifulsoup解析和搜尋元素
2. 使用selenium抓取回傳後的html，且用其工具取得html的元素值
3. 介紹xpath<br>
   https://zh.wikipedia.org/wiki/XPath
