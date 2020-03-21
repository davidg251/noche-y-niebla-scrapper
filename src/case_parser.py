from lxml.cssselect import CSSSelector
from lxml import html
from lxml.html.clean import clean_html
import json
from pprint import pprint
import re

from config import constants

class CaseParser:
  @property 
  def all_cases(self):
    return self.cases

  def __init__(self, plain_html):
    self.cases = []
    self.acts = []
    self.html_parsed = html.fromstring(plain_html)

  def load_acts(self):
    with open('acts.json') as file:
      self.acts = json.load(file)

  def	parse(self):
    tr_elements = CSSSelector("tr")(self.html_parsed)
    #remove table header
    tr_elements.pop(0)
    for tr_element in tr_elements:
      self.cases.append(self.extract_instance(tr_element))

  def extract_instance(self, tr_element):
    td_elements = CSSSelector("td")(tr_element)
    descripcion	= td_elements[0].text_content()
    fecha = td_elements[1].text_content()
    ubicacion = td_elements[2].text_content()
    victimas = self.extract_victims( td_elements[3].text_content() )
    presunto_responsable = td_elements[4].text_content()
    tipificacion = td_elements[5].text_content()
    return { "descripcion":descripcion ,
             "fecha":fecha, 
             "ubicacion":ubicacion,
             "victimas":victimas,
             "presunto_responsable":presunto_responsable,
             "tipificacion":tipificacion
           }

  def extract_victims(self, victims_field):
    all_victims = []
    victims_field = victims_field.split("|")[0]
    last_index = 0
    for m in re.finditer(constants.patternVictims, victims_field):
      victim = victims_field[last_index:m.start(0)]
      all_victims.append(
        {
          "nombre": victim,
          "casos" : self.extract_cases_victim(victim)
        }
      )
      last_index = m.start(0) + 1
    all_victims.append( {"victim": victims_field[last_index:]} )	
    return all_victims
  
  def extract_cases_victim(self, victim):
    cases_in_victim = []
    for m in re.finditer(constants.patternActsVictim, victim):
      firstIndex = victim.find(',')
      if firstIndex < 0: firstIndex = 0
      cases_in_victim.append( victim[m.start(0): m.end(0)].replace(",", "") )
    return cases_in_victim