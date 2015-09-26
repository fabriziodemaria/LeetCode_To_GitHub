import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import get_problems_links

def main(args):
	chromedriver = "/Users/fabriziodemaria/Downloads/chromedriver"
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chromedriver)
	print "Opening LeetCode..."
	driver.get("https://leetcode.com/")
	print "Executing login..."
	link = driver.find_element_by_link_text("Sign in")
	link.click()
	google = driver.find_element_by_link_text('Google')
	google.click()
	form_textfield = driver.find_element_by_id('Email')
	form_textfield.send_keys(args.email)
	nextButton = driver.find_element_by_id('next')
	nextButton.click()
	driver.implicitly_wait(3)
	form_textfield2 = driver.find_element_by_id('Passwd')
	form_textfield2.send_keys(args.password)
	nextButton = driver.find_element_by_id('signIn')
	nextButton.click()
	print "Login completed..."
	i = 0
	driver.implicitly_wait(3)
	while(True):
		driver.get("https://leetcode.com/problemset/algorithms/#")
		driver.implicitly_wait(3)
		links_to_problems = get_problems_links.get_links(driver)
		filename = links_to_problems[i].text
		links_to_problems[i].click()
		driver.implicitly_wait(3)
		nextButton = driver.find_element_by_link_text('My Submissions')
		nextButton.click()
		driver.implicitly_wait(3)
		nextButton = driver.find_element_by_partial_link_text('Accepted')
		nextButton.click()
		code_page = driver.find_element_by_tag_name("body").text
		result = code_page[code_page.find("public class Solution"):code_page.find("Back to problem")]
		f = open(str(args.path) + "/" + filename + ".java", 'w+')
		f.write(result)
		f.close
		i = i + 1
		if (i == len(links_to_problems)):
			break

	driver.close()

def parse_args():
    import argparse
    import itertools
    import sys

    parser = argparse.ArgumentParser(description='LeetCode - Google Login script.')
    parser.add_argument('email', action='store', help='email')
    parser.add_argument('password', action='store', help='password')
    parser.add_argument('path', action='store', help='password')
    if len(sys.argv)!=4:
        parser.print_help()
        sys.exit(1)
    return parser.parse_args()

if __name__ == "__main__":
    main(parse_args())
