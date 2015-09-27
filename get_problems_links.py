import os
import time
import sys
from selenium import webdriver
from selenium.webdriver.support.select import Select

def get_links(driver):
	# Problem page
	total = driver.find_element_by_xpath("//*[@id='brief_stats']/p/strong").text
	totalnumber = int(total.split(' ')[0])
	currentnumber = 0
	#print "Problems found: " + str(totalnumber)

	ff = Select(driver.find_element_by_id("filterchosen"))
	ff.select_by_visible_text("Solved Problems")
	list_of_links = []
	list_of_problems = driver.find_element_by_id("problemList").\
							  find_element_by_tag_name("tbody").\
							  find_elements_by_tag_name("tr")
	for row in list_of_problems:
		check = row.find_element_by_tag_name("td")
		if check.is_displayed():
			currentnumber = currentnumber + 1
			list_of_links.append(row.find_element_by_tag_name("a"));
			sys.stdout.write("[ " + str(float(currentnumber)/float(totalnumber)*100)[:4] + "% ] Loading... \r")
			sys.stdout.flush()
	return list_of_links

def print_links(driver):
	list_of_links = get_links(driver)
	for a in list_of_links:
		print a.text
