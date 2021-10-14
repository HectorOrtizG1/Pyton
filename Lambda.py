libros = [

    {'titulo':'El principito', 'Año':1943},
    {'titulo':'El arte de la guerra', 'Año':1772},
    {'titulo':'La ciudadad de las vestias', 'Año':2002},
    {'titulo':'El Hobbit', 'Año':1984},
    {'titulo':'El La grita', 'Año':2007}

    ]

#libros.sort()
#No podemos comparar objetos sin decir algo mas sobre ellos

#libros.sort (key = 'Año')
#Short no sabe que buscar dentro del diccionario

def ftitulo(libro):
    return libro['titulo'].upper()

def fanio(libro):
    return libro['Año']

#print(ftitulo(libros[0]))
#print(fanio(libros[0]))

print(libros)
print()
print("Libros Ordenados por año:")

#libros.sort(key=fanio)
print(libros)

print()
print("Libros Ordenados por titulo:")

#libros.sort(key=ftitulo)
print(libros)

libros.sort(key=lambda x:x['Año'])
print(libros)


