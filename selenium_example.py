from time import sleep
from selenium import webdriver


driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')


driver.get("https://www.python.org/")

sleep(5)
