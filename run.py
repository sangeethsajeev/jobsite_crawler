from crawler import Crawler



# -------------------------------------- #
# --------- Gulf Talent Website--------- #
# -------------------------------------- #
# url 	  = "https://www.gulftalent.com"

# endpoint = "/mobile/jobs/title/digital-marketing"

# element = ("div", "job-results")


# info = {"Apply Link" : {
# 				"Apply Link1":"job-results-item section",
# 				"Apply Link2":"job-results-item section section-odd"
# 				},
# 		"Job Title": "title padding-all-none space-bottom-none space-top-none line-height-15 inline",
# 		"Company Name": "company-name"}

# -------------------------------------- #
# --------- Laimoon Website------------- #
# -------------------------------------- #

url 		= "https://jobs.laimoon.com"
endpoint 	= "/uae/digital-marketing"

element = ("div", "jobgrid col-xs-12 col-sm-4 col-md-3 cont-job")

info = {
	"Apply Link" : {
			"attr"	: "class_",
			"val" : "internal-link"
	},
	"Job Title":{
			"val"  : "h4"
	},
	"Company Name" : "strong"
}

data_crawler = Crawler()
data_crawler.fetch_data(url,endpoint,element,info)