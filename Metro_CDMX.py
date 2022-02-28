from lxml import etree 
import sys

Tree = etree.parse (sys.argv [1])
NumLineas = Tree.xpath("//Document/Folder[1]/Placemark/name")
SepararLineas = []
for i in NumLineas:
    SepararLineas.append(i.text)

CoordenadasLin = Tree.xpath('//Document/Folder[1]/Placemark/LineString/coordinates')
SepararCoordenadas = []
for j in CoordenadasLin:
    SepararCoordenadas.append(j.text)

LineasCoordenadas = list(zip(SepararLineas, SepararCoordenadas))

estacion= Tree.xpath('//Document/Folder[2]/Placemark/name')
Estaciones = []
for k in estacion:
    Estaciones.append(k.text)

ubicaciones = Tree.xpath('//Document/Folder[2]/Placemark/Point/coordinates')  
ubicacion = []
for l in ubicaciones:
    Formato = l.text
    Formato = Formato.replace(' ','')
    Formato = Formato.replace('\n', '')
    ubicacion.append(Formato)

EstacionUbicacion = list(zip(Estaciones, ubicacion))

for NombreCoor in LineasCoordenadas:
    print(NombreCoor[0])
    for NombreC in EstacionUbicacion:
        if NombreC[1] in NombreCoor[1]:
            print(NombreC[0], NombreC[1])