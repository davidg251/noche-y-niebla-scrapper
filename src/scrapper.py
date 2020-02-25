import requests
import json
from config import constants

class Scrapper:

  def __init__(self, url):
    self.url = url

  def save_data(self, json_object, filename):
    try:
      output = open(filename, "w")
      output.write(json.dumps(json_object))
      output.close()
      print("archivo " + filename + " guardado con exito")
    except OSError as error:
      print ("error al escribir el archivo ")
      print (filename)
      print(error)

  def request(self, data={}, encoded=constants.raw_data):
    if data == {}:
      req = requests.get(self.url+'?'+encoded, verify=False)
    else:
      req = requests.get(self.url, verify=False, params=data)
    if(req.status_code == 200):
      print ("peticion OK")
      return req.text
    else:
      print ("fallo peticion a ", self.url)