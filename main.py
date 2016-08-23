from temp_scrapper import Scrapper
from case_parser import CaseParser

base_url = 'https://www.nocheyniebla.org/consulta_web.php'
data = data = {"evita_csrf":"uZH0XdSsJW9uwS24ZQLrdg==","presponsable":"","ffin[M]":"","ffin[d]":"","descripcion":"","caso_memo":"1","tabla":"","m_victimas":"1","mostrar":"","fini[d]":"","m_tipificacion":"1","_qf_consultaWeb_consulta":"Consulta","titulo":"","nomvic":"","sexo":"","m_ubicacion":"1","ssocial":"","fini[Y]":"","id_departamento":"91","caso_fecha":"1","ordenar":"fecha","fini[M]":"","contexto":"","ffin[Y]":"","_qf_default:consultaWeb":"consultaic=","sexo":"","fini[d]":"","fini[M]":"","fini[Y]":"","ffin[d]":"","ffin[M]":"","ffin[Y]":"","presponsable":"","contexto":"","ssocial":"","descripcion":"","ordenar":"fecha","mostrar":"tabla","caso_memo":"1","caso_fecha":"1","m_ubicacion":"1","m_victimas":"1","m_presponsables":"1","m_tipificacion":"1"}


scrapper = Scrapper(base_url)
page = scrapper.request(data)
parser = CaseParser(page)

#print parser.all_cases
#print page