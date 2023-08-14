#Listas
#Familiares

lista1 = ["Esteban","Hilaria","Cecilia","Ivana","Emilse"]

lista1.sort()

for x in lista1:
    print(x)

print(len(lista1))

lista1("Ingrese nombre abuelos")

for xx in lista1:
    print(xx)

print(len(lista1))

lista1.pop()

print


#Temperaturas
lista2_Enero = ["35","23","50","37","29"]

lista2_Enero.sort()

for x in lista2_Enero:
    print(x)

print(len(lista2_Enero))

lista2_Enero.append("Ingrese nuevo elemento")

for xx in lista2_Enero:
    print(xx)

print(len(lista2_Enero))

#Lugares

lista3 = ["Cordoba","Villa Carlos Paz","La Para","Miramar","La Falda", True]

print(lista3[0])

lista3.pop("La Para")

print

#Fechas importantes
lista4 = ["04-11-1986","10-09-1989","Nacimiento sobrino",True]

print(lista4[0])

#------------------------------------------------
#Tuplas

tupla1 = ('gato','jaguar','perro','pato')
listaA = list(tupla1)

print(listaA)

tupla2 = ('Lunes','Martes','Miercoles')
listaB = list(tupla2)

print(listaB)

tupla3 = ('febrero', 'Lucas','Marcos','Septiembre')
listaC = list(tupla3)

print(listaB)

union = zip(listaA,listaB,listaC)

print(union)

#DICCIONARIO

diccionario1 = {"14.222.255" : "Lily", "14.322.255" : "Esteban", "36.255.255":"Cecilia", "37.234.252": "Ivana", "34.355.245" : "Emilse", "07.323.142" :"Hilaria", "08.241.245":"Miguel"}

diccionario1 [""] = ""

print(diccionario1)

diccionario2 ={
    "Roman": 3513248145,
    "Joaquin": 35754545,
    "Perla": 3543248145
}
for clave, valor in diccionario2.items():
    print(clave, valor)


