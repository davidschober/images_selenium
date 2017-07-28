import selenium.webdriver as webdriver
import csv
from time import sleep

csv_file = open("top_500.csv", "r")

urls = [row[0] for row in csv.reader(csv_file)]

browser = webdriver.Chrome()

for url in urls:
    url = "%s%s" %("http://images.library.northwestern.edu", url)
    browser.get(url)
    print "working on %s" %url
    sleep(10)

