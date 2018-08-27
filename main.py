from scrapper import Scrapper
from case_parser import CaseParser
from acts_parser import ActsParser


# there are two ways for query the data, with the params raw in the url or
# with params in the request's body. 
base_url = 'https://base.nocheyniebla.org/consulta_web.php'
data = {"evita_csrf":"uZH0XdSsJW9uwS24ZQLrdg==","presponsable":"103","ffin[M]":"","ffin[d]":"","descripcion":"","caso_memo":"1","tabla":"","m_victimas":"1","mostrar":"","fini[d]":"","m_tipificacion":"1","_qf_consultaWeb_consulta":"Consulta","titulo":"","nomvic":"","sexo":"","m_ubicacion":"1","ssocial":"","fini[Y]":"","id_departamento":"76","id_municipio":"616","caso_fecha":"1","ordenar":"fecha","fini[M]":"","contexto":"","ffin[Y]":"","_qf_default:consultaWeb":"consultaic=","sexo":"","fini[d]":"","fini[M]":"","fini[Y]":"","ffin[d]":"","ffin[M]":"","ffin[Y]":"","presponsable":"103","contexto":"","ssocial":"","descripcion":"","ordenar":"fecha","mostrar":"tabla","caso_memo":"1","caso_fecha":"1","m_ubicacion":"1","m_victimas":"1","m_presponsables":"1","m_tipificacion":"1"}
raw_data = "evita_csrf=%2FEl5dGqjXZgB%2B%2FAf33srYw%3D%3D&_qf_default=consultaWeb%3Aconsulta&titulo=&id_departamento=76&id_municipio=&nomvic=&sexo=&fini%5Bd%5D=&fini%5BM%5D=&fini%5BY%5D=&ffin%5Bd%5D=&ffin%5BM%5D=&ffin%5BY%5D=&presponsable=&contexto=&clasificacion%5B%5D=A%3A1%3A10&ssocial=1&descripcion=&critetiqueta=0&poretiqueta=&critetiqueta2=0&poretiqueta2=&ordenar=fecha&mostrar=tabla&caso_memo=1&caso_fecha=1&m_ubicacion=1&m_victimas=1&m_presponsables=1&m_tipificacion=1&_qf_consultaWeb_consulta=Consulta"

def extract_acts():
  scrapper = Scrapper(base_url)
  #when the url is requested without data, the search form is retrieved
  home_page = scrapper.request({})
  acts_scrapper = ActsParser(home_page)
  acts_scrapper.parse()
  scrapper.save_data(acts_scrapper.acts ,"acts.json")

def extract_cases():
  scrapper = Scrapper(base_url)
  home_page = scrapper.request()
  cases_scrapper = CaseParser(home_page)
  cases_scrapper.parse()
  scrapper.save_data(cases_scrapper.cases ,"cases.json")

extract_cases()
#extract_acts()