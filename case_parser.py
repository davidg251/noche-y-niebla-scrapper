from lxml.cssselect import CSSSelector
from lxml import html
from lxml.html.clean import clean_html
import json
from pprint import pprint

class CaseParser:


	@property 
	def all_cases(self):
		return self.all_cases



	def __init__(self, plain_html):

		#self.html_parsed = None
		self.all_cases = []
		self.html_parsed = html.fromstring(plain_html)
		self.acts = []
			


	def load_acts(self):
		
		with open('acts.json') as file:    
			self.acts = json.load(file)



	def	parse(self):

		tr_elements = CSSSelector("tr")(self.html_parsed)
		#remove table header
		tr_elements.pop(0)

		for tr_element in tr_elements:
			self.all_cases.append(self.extract_instance(tr_element))
			print "##############################"



	def extract_instance(self, tr_element):

		td_elements = CSSSelector("td")(tr_element)
		
		descripcion	= td_elements[0].text_content()
		fecha = td_elements[1].text_content()
		ubicacion = td_elements[2].text_content()
		victimas = self.extract_victims( td_elements[3].text_content() )
		presunto_responsable = td_elements[4].text_content()
		tipificacion = td_elements[5].text_content()

		return {"descripcion":descripcion , "fecha":fecha, "ubicacion":ubicacion, "victimas":victimas, "presunto_responsable":presunto_responsable, "tipificacion":tipificacion}



	def extract_victims(self, victims_field):
		#esto cambia por regexp
		self.load_acts()
		victims = victims_field.split("|")
		victims = victims[0].split(",")
		print victims
		victims_object = []
		victim = None
		actsxvcitim = []
		i = 1


		if ( len(victims) is 1) :
			#cuando es solo una victima
			vict = victims[0].split(" ") 
			act = vict.pop()
			vict = ''.join(el+'' for el in vict)

			victims_object.append({"victima":vict, "actos":act})
			return victims_object

		for elem in victims:
			
			elem = elem.strip()



			elif( not(elem in self.acts) ) :#si es victima

				vict = elem.split(" ") 
				act = vict.pop()
				vict = ''.join(el+" " for el in vict)

				if(victim is None):
					victim = vict
					actsxvcitim.append(act)
				
				else:
					victims_object.append( {"victima":vict,"actos":actsxvcitim} )
					victim = vict
					actsxvcitim = []		


			else :#si es acto

				actsxvcitim.append(elem)

			i+=1

		#print "############################"
		#pprint(victims)		
		pprint(victims_object)
		#print "############################"		
		return victims
