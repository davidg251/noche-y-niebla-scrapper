import requests
import json

class Scrapper:

  def __init__(self, url):
    self.url = url

  def save_data(self, json_object, filename):
    try:
      output = open(filename, "w")
      output.write(json.dumps(json_object))
      output.close()
      print("archivo "+filename+" guardado con exito")
    except OSError as error:
      print ("error al escribir el archivo ")
      print (filename)
      print(error)

  def request(self, data={}, encoded="evita_csrf=%2FEl5dGqjXZgB%2B%2FAf33srYw%3D%3D&_qf_default=consultaWeb%3Aconsulta&titulo=&id_departamento=76&id_municipio=&nomvic=&sexo=&fini%5Bd%5D=&fini%5BM%5D=&fini%5BY%5D=&ffin%5Bd%5D=&ffin%5BM%5D=&ffin%5BY%5D=&presponsable=&contexto=&clasificacion%5B%5D=A%3A1%3A10&ssocial=1&descripcion=&critetiqueta=0&poretiqueta=&critetiqueta2=0&poretiqueta2=&ordenar=fecha&mostrar=tabla&caso_memo=1&caso_fecha=1&m_ubicacion=1&m_victimas=1&m_presponsables=1&m_tipificacion=1&_qf_consultaWeb_consulta=Consulta"):
    if data == {}:
      req = requests.get(self.url+'?'+encoded, verify=False)
    else:
      req = requests.get(self.url, verify=False, params=data)
    if(req.status_code == 200):
      print ("peticion OK")
      return req.text
    else:
      print ("fallo peticion a ", self.url)