import re

from scrapper import Scrapper
from case_parser import CaseParser
from acts_parser import ActsParser
from config import constants

# there are two ways for query the data, with the params raw in the url or
# with params in the request's body. 
def extract_acts():
  scrapper = Scrapper(constants.base_url)
  #when the url is requested without data, the search form is retrieved
  home_page = scrapper.request({})
  acts_scrapper = ActsParser(home_page)
  acts_scrapper.parse()
  scrapper.save_data(acts_scrapper.acts ,"acts.json")

def extract_cases():
  scrapper = Scrapper(constants.base_url)
  home_page = scrapper.request()
  cases_scrapper = CaseParser(home_page)
  cases_scrapper.parse()
  scrapper.save_data(cases_scrapper.cases ,"cases.json")

extract_cases()
#extract_acts()