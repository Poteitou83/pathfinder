import xmltodict
import extract
import sys
import helper
orig_stdout = sys.stdout
f = open("../data/border.txt", "w")
graphml = open("../data/map3.graphml", "+br")
xmldoc = xmltodict.parse(graphml, xml_attribs=True)
sys.stdout = f
ways = ["832455068", "832455091", "832455017", "832455027", "832454977", "1001979393"]
def getBorder(wayId):
    nodes = []
    visited = {}
    for edge in xmldoc["graphml"]["graph"]["edge"]:
        isWay = 0
        for datum in edge["data"]:
            if datum["@key"] == "d7":
                if (datum["#text"] == wayId):
                    location = helper.getLatLon(edge["@source"])
                    if (location not in visited):
                        nodes.append([location[0], location[1]])
                        visited[location] = 1
                    isWay = 1
            if datum["@key"] == "d16" and isWay:
                betweenNodes = extract.extractLineString(datum["#text"])
                for node in betweenNodes:
                    if (node not in visited):
                        nodes.append([node[0], node[1]])
                        visited[node] = 1
        if isWay:
            location = helper.getLatLon(edge["@target"])
            if (location not in visited):
                nodes.append([location[0], location[1]])
                visited[location] = 1
    if (len(nodes)):
        print(nodes)
    

for way in ways:
    getBorder(way)
            