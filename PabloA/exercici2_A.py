#Creem el diccionari
myDict= {}

#Anem afegint contingut al mateix
myDict['Edat'] = 19 
myDict['Estudis'] = 'Batxillerat'
myDict['Mundials'] = 3
myDict['Telefon'] = 689123341
myDict['Germans'] = 2
myDict['Pes'] = 65

#Que imprimeixi per pantalla la longitud del diccionari
print(len(myDict))

#Valors del diccionari
print(myDict.values())

#Últim item del diccionari
print(myDict.popitem())