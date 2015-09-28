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
	driver.implicitly_wait(10)
	form_textfield2 = driver.find_element_by_id('Passwd')
	form_textfield2.send_keys(args.password)
	nextButton = driver.find_element_by_id('signIn')
	nextButton.click()
	print "Login completed..."
	i = 0
	driver.implicitly_wait(2000)

	while(True):
		driver.get("https://leetcode.com/problemset/algorithms/#")
		driver.implicitly_wait(2000)
		links_to_problems = get_problems_links.get_links(driver)
		filename = links_to_problems[i].text
		links_to_problems[i].click()
		driver.implicitly_wait(2000)
		nextButton = driver.find_element_by_link_text('My Submissions')
		nextButton.click()
		driver.implicitly_wait(2000)
		nextButton = driver.find_element_by_partial_link_text('Accepted')
		nextButton.click()
		driver.implicitly_wait(2000)
		code_page = driver.find_element_by_tag_name("body").text
		driver.implicitly_wait(2000)
		if "Language: python" in code_page:
			result = code_page[code_page.find("class "):code_page.find("Back to problem")]
			print "====================================\n" + filename + "\n====================================\n"
			print result
			f = open(str(args.path) + "/" + filename + ".py", 'w+')
			f.write(result)
			f.flush()
			driver.implicitly_wait(2000)
			f.close
		if "Language: java" in code_page:
			result = code_page[code_page.find("class "):code_page.find("Back to problem")]
			print "====================================\n" + filename + "\n====================================\n"
			print result
			f = open(str(args.path) + "/" + filename + ".java", 'w+')
			f.write(result)
			driver.implicitly_wait(2000)
			f.flush()
			f.close
		i = i + 1
		if (i == len(links_to_problems)):
			break
	# TODO check resulting files' dimensions to verify errors in getting the source code
	driver.close()

def parse_args():
    import argparse
    import itertools
    import sys

    parser = argparse.ArgumentParser(description='LeetCode - Google Login script.')
    parser.add_argument('email', action='store', help='email')
    parser.add_argument('password', action='store', help='password')
    parser.add_argument('path', action='store', help='Path to save files')
    if len(sys.argv)!=4:
        parser.print_help()
        sys.exit(1)
    return parser.parse_args()

if __name__ == "__main__":
    main(parse_args())
