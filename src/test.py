import xmltodict
import helper as help
import sys
graphml = open("../data/map3.graphml", "+br")

xmldoc = xmltodict.parse(graphml, xml_attribs = True)
orig_stdout = sys.stdout
f = open("../data/out4.txt", "w")
sys.stdout = f

road = {"primary":0, "secondary":0, "tertiary":0, "unclassified":0, "residential": 0}
edges = xmldoc["graphml"]["graph"]["edge"]
nodes = {}
for edge in edges:
    for datum in edge["data"]:
        if (datum["@key"] == "d14"):
            if (datum["#text"] not in road):
                continue
            (lat, lon) = help.getLatLon(edge["@source"])
            if ((lat, lon) not in nodes):
                print(str(lat) + " " + str(lon))
                nodes[(lat, lon)] = 0
            (lat, lon) = help.getLatLon(edge["@target"])
            if ((lat, lon) not in nodes):
                print(str(lat) + " " + str(lon))
                nodes[(lat, lon)] = 0

sys.stdout = orig_stdout
f.close()
    

