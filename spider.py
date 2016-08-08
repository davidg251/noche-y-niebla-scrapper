import requests
from lxml.cssselect import CSSSelector
from lxml import html
from lxml.html.clean import clean_html
import json
from pprint import pprint

events = []

def parser(html_plain):
	
	html_parsed = html.fromstring(html_plain)
	rows = CSSSelector("tr")(html_parsed)

	for row in rows:
		
		temp = ""		
		columns = CSSSelector("td")(row)
		
		for column in columns:
			temp += "--"+column.text_content()+"--"

		events.append(temp)

URL = 'https://www.nocheyniebla.org/consulta_web.php'

data = {'evita_csrf':'uZH0XdSsJW9uwS24ZQLrdg==','presponsable':'','ffin[M]':'','ffin[d]':'','descripcion':'','caso_memo':'1','tabla':'','m_victimas':'1','mostrar':'','fini[d]':'','m_tipificacion':'1','_qf_consultaWeb_consulta':'Consulta','titulo':'','nomvic':'','sexo':'','m_ubicacion':'1','ssocial':'','fini[Y]':'','id_departamento':'91','caso_fecha':'1','ordenar':'fecha','fini[M]':'','contexto':'','ffin[Y]':'','_qf_default:consultaWeb':'consultaic=','sexo':'','fini[d]':'','fini[M]':'','fini[Y]':'','ffin[d]':'','ffin[M]':'','ffin[Y]':'','presponsable':'','contexto':'','ssocial':'','descripcion':'','ordenar':'fecha','mostrar':'tabla','caso_memo':'1','caso_fecha':'1','m_ubicacion':'1','m_victimas':'1','m_presponsables':'1','m_tipificacion':'1'}

r = requests.get(URL, verify=False, params=data)
"""
print "url"
print r.url
print "body response: "
print r.text
print "cookies: "
print r.cookies
print "headers: "
print r.headers
print "code response: "
print r.status_code"""


parser(r.text)
pprint(events)