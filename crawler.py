from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup,NavigableString
import sys
import configparser
import time

class Crawler(object):

	def __init__(self):
		self.url 		= ""
		self.element_id = ""
		self.info_obj 	= dict()

	def get_browser(self):
		# option = webdriver.firefox.options.Options()
		# option.headless = True
		# option.incognito = True
		option = webdriver.ChromeOptions()
		option.add_argument("--headless")
		option.add_argument("--incognito")
		try:
			# browser = webdriver.Firefox(executable_path = '/Users/sangeethsajeev/.wdm/drivers/geckodriver/macos/v0.27.0/geckodriver'
			# ,options=option)
			browser = webdriver.Chrome(ChromeDriverManager().install()
				,chrome_options=option)
			try:
				time.sleep(5)
				browser.get(self.url)
				webdriver.support.ui.WebDriverWait(browser,7)
				return browser
			except Exception as e:
				print("Unable to get url:",e)
		except Exception as e:
			print("Unable to init Web Driver:",e)
			return None

	def list_out_dict(self,info_obj):
		for i in self.info_obj:
			for j in info_obj[i]:
				print(i,"-->",j,"---->",info_obj[i][j])


	def check_page(self,url,endpoint):
		browser = self.get_browser()
		if(browser):
			browser.get(url+endpoint)
			soup = BeautifulSoup(browser.page_source,features="lxml")
			print(soup.prettify())
			browser.quit()


	def store_in_object(self,index,info_str,info_key):
		# print(info_key)
		# print(info_str)
		# print(self.info_obj)
		try:
			if(index in self.info_obj):
				obj_dict = dict(self.info_obj[index])
				if(info_key in obj_dict):
					obj_dict[info_key].append(info_str)
				else:
					obj_dict[info_key] = [info_str]

				self.info_obj[index] = obj_dict
			else:
				obj_dict = dict()
				obj_dict[info_key] = [info_str]
				self.info_obj[index] = obj_dict

			# print("Dict: ",self.info_obj)

		except Exception as e:
			print("Store Object Error:",e)

	def fetch_data(self,url,endpoint,element,info):
		self.url 		= url+endpoint
		self.element_id = element
		print(self.url)
		print(self.element_id)
		browser 		= self.get_browser()

		if(browser):
			soup=BeautifulSoup(browser.page_source,features="lxml")
			for tags_info in soup.find_all(element[0],class_=element[1]):
				if isinstance(tags_info,NavigableString):
					continue
				print("----------------------------")
				for i in info:
					ind=0
					if i == "Apply Link":
						link = dict(info[i])
						# print(link)
						for l in link:
							for tags in tags_info.find_all(class_ = link[l]):
								ind+=1
								# info_str = str(url+str(tags['href'].strip()))
								info_str = str(tags['href'].strip())
								info_key = "Apply Link"
								index 	 = ind
								print(ind,info_str,info_key)
								self.store_in_object(index,info_str,info_key)
					else:
						for tags in tags_info.find_all(class_ = info[i]):
							ind+=1
							info_str = tags.get_text().strip()
							info_key = i
							index = ind
							print(ind,info_str,info_key)
							self.store_in_object(index,info_str,info_key)
					
				print("-----------------------------")

			self.list_out_dict(self.info_obj)
			browser.quit()
		else:
			print("Unable to fetch_data")