from pymongo import MongoClient
import pymongo
import matplotlib.pyplot as plt 
from datos_pais import *



cliente=MongoClient()
#print(cliente.list_database_names()) #Todas las bases de datos que tenemos
db=cliente.Corona
#print(db.list_collection_names()) #Todas las colecciones de la base de datos Corona



#Apartado 1:

todo=db.paises.find()

#Comento las siguientes lineas para no tener que mostrar todos los datos siempre
#for dato in todo:
#    print(dato)

#Apartado 2:
print("Buscamos los datos de España en Marzo")
datosespana=db.paises.find({"geoId": "ES", "month": 3}, {"_id": 0})

for dia in datosespana:
    print(dia)

#Apartado 3:
x,y,a=datos_por_pais(db.paises, "ES")
plt.plot(x,y,'r',x,a,'r--')

#Apartado 4:
x1,y1,a1=datos_por_pais(db.paises, "IT")
plt.plot(x1,y1,'b',x1,a1,'b--')
x1,y1,a1=datos_por_pais(db.paises, "DE")
plt.plot(x1,y1,'y',x1,a1,'y--')
x1,y1,a1=datos_por_pais(db.paises, "FR")
plt.plot(x1,y1,'o',x1,a1,'o--')
plt.show()

#Apartado 5:

print("Apartado 5 ----------------------------")
grupo=db.paises.aggregate([{"$group": {"_id": "$geoId", "cuantos": {"$sum": 1}}}])

for g in grupo:
    print(g)

#Apartado 6:
print("Apartado 6 ------------------------------------")
grupo=db.paises.aggregate([{"$group":{"_id":"$geoId", "total":{"$sum":"$cases"}}},{"$sort":{"total":1}}])

for g in grupo:
    print(g)

#Apartado 7:
print("Apartado 7 ------------------------------------")
grupo=db.paises.aggregate([{"$match":{"geoId":{"$in": ["ES","IT","FR","DE"]}}},
    {"$group":{"_id": "$geoId", "total": {"$sum": "$cases"}}},
    {"$sort": {"total":1}}])

for g in grupo:
    print(g)