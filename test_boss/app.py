import time
import csv
from selenium import webdriver
from lxml import etree

options = webdriver.ChromeOptions()
options.add_argument("User-Agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
# options.add_argument('--proxy-server=http://127.0.0.1:4780')
# options.add_experimental_option("debuggerAddress","127.0.0.1:9222")

driver =webdriver.Chrome(options=options)
driver.implicitly_wait(3)
driver.get("https://www.zhipin.com/web/geek/job?query=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&city=101020100")

# search_tag = driver.find_element(By.CSS_SELECTOR,'.ipt-search')
# search_tag.send_keys("前端开发")

# btn = driver.find_element(By.CSS_SELECTOR,'.btn-search')
# btn.click()

time.sleep(10)

f = open('boss.csv', "w", -1, encoding="utf-8", newline="")
csv.writer(f).writerow([
	"职位",
	"位置",
	"薪资",
	"联系人",
	"经验",
	"公司名",
	"类型",
	"职位技能",
	"福利",
	"详情页"
])

jobList = []

def parse():

	tree = etree.HTML(driver.page_source)
	jobs = tree.xpath("//div[@class='search-job-result']/ul/li")

	for i in jobs:
		jobName = i.xpath(".//span[@class='job-name']/text()")[0]
		jobList.append(
			{
				"jobName": jobName
			}
		)

parse()
driver.quit()

print(jobList)