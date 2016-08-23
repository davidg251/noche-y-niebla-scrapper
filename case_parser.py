from lxml.cssselect import CSSSelector
from lxml import html
from lxml.html.clean import clean_html

class CaseParser:


	def __init__(self, plain_html):

		self.html_parsed = None
		self.all_cases = []
		html_parsed = html.fromstring(plain_html)
		tr_elements = CSSSelector("tr")(html_parsed)

		#remove table header
		tr_elements.pop(0)

		for tr_element in tr_elements:

			self.all_cases.append(self.extract_instance(tr_element))
			

	@property 
	def all_cases(self):
		return self.all_cases

	def extract_instance(self, tr_element):

		td_elements = CSSSelector("td")(tr_element)
		
		descripcion 			= td_elements[0].text_content();
		fecha 					= td_elements[1].text_content();
		ubicacion 				= td_elements[2].text_content();
		victimas 			 	= td_elements[3].text_content();
		presunto_responsable 	= td_elements[4].text_content();
		tipificacion 			= td_elements[5].text_content();

		return {"descripcion":descripcion , "fecha":fecha, "ubicacion":ubicacion, "victimas":victimas, "presunto_responsable":presunto_responsable, "tipificacion":tipificacion}


	def extract_victims(victims_field):
	
		victims = victims_field.split(",")
		return victims
