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
    except OSError as error:
      print ("error al escribir el archivo ")
      print (filename)
      print(error)

  def request(self, data):
    req = requests.get(self.url, verify=False, params=data)
    if(req.status_code == 200):
      print ("haciendo peticion.. ")
      print (req.url)
      return req.text
    else:
      print ("fallo peticion a ")
      print (self.url)