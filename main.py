from temp_scrapper import Scrapper
from case_parser import CaseParser
from acts_parser import ActsParser


base_url = 'https://www.nocheyniebla.org/consulta_web.php'
data = {"evita_csrf":"uZH0XdSsJW9uwS24ZQLrdg==","presponsable":"","ffin[M]":"","ffin[d]":"","descripcion":"","caso_memo":"1","tabla":"","m_victimas":"1","mostrar":"","fini[d]":"","m_tipificacion":"1","_qf_consultaWeb_consulta":"Consulta","titulo":"","nomvic":"","sexo":"","m_ubicacion":"1","ssocial":"","fini[Y]":"","id_departamento":"76","id_municipio":"616","caso_fecha":"1","ordenar":"fecha","fini[M]":"","contexto":"","ffin[Y]":"","_qf_default:consultaWeb":"consultaic=","sexo":"","fini[d]":"","fini[M]":"","fini[Y]":"","ffin[d]":"","ffin[M]":"","ffin[Y]":"","presponsable":"","contexto":"","ssocial":"","descripcion":"","ordenar":"fecha","mostrar":"tabla","caso_memo":"1","caso_fecha":"1","m_ubicacion":"1","m_victimas":"1","m_presponsables":"1","m_tipificacion":"1"}

def extract_acts():
  scrapper = Scrapper(base_url)
  #when the url is requested without data, the search form is retrieved
  home_page = scrapper.request({})
  acts_scrapper = ActsParser(home_page)
  acts_scrapper.parse()
  scrapper.save_data(acts_scrapper.acts ,"acts.json")

def extract_cases():
  scrapper = Scrapper(base_url)
  home_page = scrapper.request(data)
  cases_scrapper = CaseParser(home_page)
  cases_scrapper.parse()
  scrapper.save_data(cases_scrapper.acts ,"cases.json")

extract_cases()