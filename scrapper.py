import requests
from lxml.cssselect import CSSSelector
from lxml import html
from lxml.html.clean import clean_html
import json
from pprint import pprint

	
all_cases = []


def extract_instance(tr_element):

	td_elements = CSSSelector("td")(tr_element)
	
	descripcion 			= td_elements[0].text_content();
	fecha 					= td_elements[1].text_content();
	ubicacion 				= td_elements[2].text_content();
	victimas 			 	= td_elements[3].text_content();
	presunto_responsable 	= td_elements[4].text_content();
	tipificacion 			= td_elements[5].text_content();

	return {"descripcion":descripcion , "fecha":fecha, "ubicacion":ubicacion, "victimas":victimas, "presunto_responsable":presunto_responsable, "tipificacion":tipificacion}



def parser(html_plain):

	html_parsed = html.fromstring(html_plain)
	tr_elements = CSSSelector("tr")(html_parsed)

	#remove the header of table
	tr_elements.pop(0)

	for tr_element in tr_elements:

		all_cases.append(extract_instance(tr_element))



def save_data():
	
	output = open("cases.json", "w")
	output.write(json.dumps(all_cases)+"\n")
	output.close()


URL = 'https://www.nocheyniebla.org/consulta_web.php'

data = {"evita_csrf":"uZH0XdSsJW9uwS24ZQLrdg==","presponsable":"","ffin[M]":"","ffin[d]":"","descripcion":"","caso_memo":"1","tabla":"","m_victimas":"1","mostrar":"","fini[d]":"","m_tipificacion":"1","_qf_consultaWeb_consulta":"Consulta","titulo":"","nomvic":"","sexo":"","m_ubicacion":"1","ssocial":"","fini[Y]":"","id_departamento":"91","caso_fecha":"1","ordenar":"fecha","fini[M]":"","contexto":"","ffin[Y]":"","_qf_default:consultaWeb":"consultaic=","sexo":"","fini[d]":"","fini[M]":"","fini[Y]":"","ffin[d]":"","ffin[M]":"","ffin[Y]":"","presponsable":"","contexto":"","ssocial":"","descripcion":"","ordenar":"fecha","mostrar":"tabla","caso_memo":"1","caso_fecha":"1","m_ubicacion":"1","m_victimas":"1","m_presponsables":"1","m_tipificacion":"1"}

r = requests.get(URL, verify=False, params=data)

if(r.status_code == 200):
	
	parser(r.text)
	pprint(all_cases)
	save_data()
	print "saved"
	
else:
	
	print "fail request"


"""
debug request
print "body response: "
print r.text
print "cookies: "
print r.cookies
print "headers: "
print r.headers
print "url"
print r.url
print "code response: "
print r.status_code
"""
