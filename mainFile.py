from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
url="https://www.facebook.com"

class mainFile:

    def driv(self,driver,url):
        self.d = driver
        self.d.get(url)

#    def brows(self,url):



obj = mainFile()
obj.driv(driver,url)

#obj.brows(url)