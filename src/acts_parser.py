from lxml.cssselect import CSSSelector
from lxml import html
from lxml.html.clean import clean_html
from pprint import pprint

class ActsParser:

  def __init__(self, plain_html):
    self.acts = []
    self.html_parsed = html.fromstring(plain_html)

  def parse(self):
    select_element = CSSSelector("[name=\"clasificacion[]\"]")(self.html_parsed)
    option_elements = CSSSelector("option")(select_element[0])
    for el in option_elements:
      self.acts.append( el.text_content().split(":")[0] )