import csv
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("User-Agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)

# 隐式等待
# driver.implicitly_wait(3)
driver.get("https://www.zhipin.com/web/geek/job?query=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&city=101020100")

# 显示等待
WebDriverWait(driver, 10).until(
	EC.presence_of_element_located((By.XPATH, '//*[@class="page-job-wrapper"]'))
)

# search_tag = driver.find_element(By.CSS_SELECTOR,'.ipt-search')
# search_tag.send_keys("前端开发")

# btn = driver.find_element(By.CSS_SELECTOR,'.btn-search')
# btn.click()

jobList = []

def parse():

	tree = etree.HTML(driver.page_source)
	jobs = tree.xpath("//div[@class='search-job-result']/ul/li")

	for i in jobs:
		name = i.xpath(".//span[@class='job-name']/text()")[0]
		address = i.xpath(".//span[@class='job-area']/text()")[0]
		salary = i.xpath(".//span[@class='salary']/text()")[0]
		hr = i.xpath(".//div[@class='info-public']/text()")[0]
		exp = i.xpath(".//ul[@class='tag-list']/li/text()")[0]
		company = i.xpath(".//h3[@class='company-name']/a/text()")[0]
		good = i.xpath(".//div[@class='info-desc']/text()")
		goodList = list(good)
		companyInfo = i.xpath(".//ul[@class='company-tag-list']/li/text()")
		skill = i.xpath(".//div[@class='job-card-footer clearfix']/ul/li/text()")
		
		jobList.append(
			{
				"职位": name,
				"位置": address,
				"薪资": salary,
				"联系人": hr,
				"经验": exp,
				"公司名": company,
				"类型": ','.join(companyInfo),
				"职位技能": ",".join(skill),
				"福利": goodList[0] if len(goodList) > 0  else ''
			}
		)

parse()
driver.quit()

f = open('boss.csv', "w", -1, encoding="utf-8", newline="")
header = [
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
]
writer = csv.DictWriter(f, header)
writer.writeheader()

writer.writerows(jobList)
# print(jobList)