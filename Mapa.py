from lxml import etree # https://lxml.de/
import math

with open("map.osm",encoding='UTF8') as f:
    xml_srt = f.read()
    xml_srt = xml_srt.encode('UTF8')

class Node():
    def __init__(self,id,lat,lon,tags):
        self.id = id
        self.lat = lat
        self.lon = lon
        self.tags = tags
    def __repr__(self):
        return f"{self.id, self.lat, self.lon, self.tags}"
    def __str__(self):
        return Node(self.id, self.lat, self.lon, self.tags)
    def cord(self):
        return (float(self.lat), float(self.lon))

class Way():
    def __init__(self,id,tags,nodes):
        self.id = id
        self.tags = tags
        self.nodes = nodes
        self.oneway = False
    def __repr__(self):
        return f"{self.id, self.tags, self.nodes}"
    def __str__(self):
        return f"{self.id, self.tags, self.nodes}"

nodes = []
ways = []
root = etree.fromstring(xml_srt)

def GetNodesChildren():
    for element in root.getchildren():
        if element.tag != "node" : continue
        attrib = element.attrib
        tags_dict = {}
        for tag in element.getchildren():
            tags_dict[tag.attrib["k"]] = tag.attrib["v"]
        node = Node(
            id=attrib["id"],
            lat=attrib["lat"],
            lon=attrib["lon"],
            tags=tags_dict
        )
        nodes.append(node)

def GetWays():
    for element in root.getchildren():
        if element.tag != "way" : continue
        attrib = element.attrib 

        via = Way(
            id=attrib['id'],
            tags=list(),
            nodes=list()
            )
        for tag in element.getchildren():
                
            if tag.tag == 'tag':
                via.tags.append(tag.tag)
                if(tag.attrib["k"] == 'oneway' and tag.attrib["v"] == 'yes'):
                    via.oneway == True



            if tag.tag == 'nd':
                for node in nodes:
                    if node.id == tag.attrib['ref']:
                        via.nodes.append(node)
                        
        ways.append(via)    

class Edge():
    def __init__(self,firstNode,secondNode,oneway):
        self.firstNode = firstNode
        self.secondNode = secondNode
        self.oneway = oneway
    def __repr__(self):
        return f"{self.firstNode, self.secondNode}"
    def __str__(self):
        return f"{self.firstNode, self.secondNode}"
    def cost(self):
        # https://noticias.coches.com/consejos/medir-distancia-dos-puntos/462887
        return math.sqrt((float(self.firstNode.lon) - float(self.secondNode.lon))**2 + (float(self.firstNode.lat) - float(self.secondNode.lat))**2)

GetNodesChildren()
GetWays()
# print(ways)

class Graph():
    def __init__(self,ways):
        self.edges = []
        self.adyacencia = {}
        for way in ways:
            for index in range(len(way.nodes)):
                try:
                    edge = Edge(way.nodes[index],way.nodes[index+1],way.oneway)
                    self.add(edge)
                except:
                    pass

    def add(self,edge):
        if edge not in self.edges:
            self.edges.append(edge)
            self.addAdyacencia(edge)
    
    def getAdyacencia(self):
        return self.adyacencia
    def addAdyacencia(self,edge:Edge):
        firstNode = edge.firstNode.cord()
        secondNode = edge.secondNode.cord()
        
        if firstNode in self.adyacencia:
            self.adyacencia[firstNode].append([secondNode, edge.cost()])
            if not edge.oneway:
                if secondNode not in self.adyacencia:
                    self.adyacencia.setdefault(secondNode, [[firstNode, edge.cost()]])
                else:

                    self.adyacencia[secondNode].append([firstNode, edge.cost()])

        else:
            if edge.oneway:
                self.adyacencia.setdefault(firstNode, [[secondNode, edge.cost()]])
            else:
                self.adyacencia.setdefault(firstNode, [[secondNode, edge.cost()]])

                if secondNode not in self.adyacencia:

                    self.adyacencia.setdefault(secondNode, [[firstNode, edge.cost()]])
                else:

                    self.adyacencia[secondNode].append([firstNode, edge.cost()])
