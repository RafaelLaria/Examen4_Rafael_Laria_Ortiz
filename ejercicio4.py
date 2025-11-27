def mejor_estudiante_mates(lista_alumnos):
    nombre_mejor = ""
    mejor_nota = -1

    for a in lista_alumnos:
        nota = a['notas']['Mates']
        nombre = a['nombre']

        if nota > mejor_nota:
            nombre_mejor = nombre
            mejor_nota = nota
    return nombre_mejor, mejor_nota
alumnos = [
{"nombre": "Ana", "notas": {"Mates": 8, "Lengua": 9}},
{"nombre": "Luis", "notas": {"Mates": 4, "Lengua": 5}},
{"nombre": "Eva", "notas": {"Mates": 9, "Lengua": 8}}
]
print(mejor_estudiante_mates(alumnos))
