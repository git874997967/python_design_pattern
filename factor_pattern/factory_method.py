import xml.etree.ElementTree as etree
import json 

class JSONConnector:
    def __init__(self,filePath):
        self.filePath = filePath
        self.data = dict()
        with open(self.filePath,'r+',encoding= 'utf-8') as file:
          self.data = json.load(file)
    @property
    def parse_data(self):
      return self.data
class XMLConnector:
    def __init__(self,filePath):
        self.filePath = filePath
        self.data = etree.parse(self.filePath)
    @property
    def parse_data(self):
        return self.data


def connection_factory(filePath):
    filePath = str(filePath)
    if filePath.endswith('xml'):
        return XMLConnector(filePath)
    elif filePath.endswith('json'):
        return JSONConnector(filePath)
    else:
        raise ValueError(f"Cannot connect to {filePath}")
    
def connect_to(filePath):
    factory = None
    try:
        factory = connection_factory(filePath)
    except ValueError as ve:
        print(ve)
    return factory

def main():
    sql_factory = connect_to('data/person.sq3')
    print()
    xml_factory = connect_to('data/person.xml')
    xml_data = xml_factory.parse_data
    liars = xml_data.findall(f".//{'person'}[{'lastName'}='{'Liar'}']")
    print(f"fount {len(liars)} persons")
    for liar in liars:
        print(f"first Name: {liar.find('firstName').text}")
        print(f"last Name: {liar.find('lastName').text}")
        [print(f"phone Number ({p.attrib['type']}) {p.text}") for p in liar.find("phoneNumbers")]
    json_factory = connect_to('data/dount.json')
    json_data = json_factory.parse_data
    print(f"found {len(json_data)} dounts")
    for dount in json_data:
        print(f"name: {dount['name']}")
        print(f"price: {dount['ppu']}")
        [print(f"topping: {i['id']}, {i['type']}") for i in dount['topping']]
if __name__ == "__main__":
    main()


