import os
from selenium import webdriver

chromedriver = "/Users/fabriziodemaria/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https://leetcode.com/problemset/algorithms/")
list_of_links = driver.find_elements_by_tag_name("a")
for link in list_of_links:
	print link.text
driver.close()
