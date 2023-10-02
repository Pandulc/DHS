# Ejercicios 1 al 3 de la guia extra
def EJE4_1to3(K, V):
    d = {}
    # Metodo con for iterado
    # i = 0
    # for key in K:
    #    d[key] = V[i]
    #    i += 1
    # print(d)

    # Metodo con zip y for
    # for e in zip(K,V):
    #   d[e[0]] = e[1]
    # print(d)

    # Metodo con zip y dic
    d = dict(zip(K, V))
    print(d)

    # Ejercicio 2

    key = "Cuarenta"
    value = 40

    d[key] = value
    print(d)

    # Ejercicio 3

    del d["Veinte"]
    print(d)

# EJE4_1to3(["Diez", "Veinte", "Treinta"], [10, 20, 30])

# Ejercicios 4 a 7 de la guia extra


def EJE4_4to7(n, a, l, M):
    # Ejercicio 4
    estudiante = {"Nombre": n, "Apellido": a, "Legajo": l, "Materias": M}
    print(estudiante)

    # Ejercicio 5
    estudiante["Legajo"] = 1584
    newMaterias = estudiante["Materias"][:]
    newMaterias.append("Musica")
    newMaterias.append("Biologia")
    estudiante["Materias"] = newMaterias
    print(estudiante)

    # Ejercicio 6
    i = 0
    dicMaterias = {}
    for materia in estudiante["Materias"]:
        dicMaterias[i] = materia
        i += 1
    estudiante["Materias"] = dicMaterias
    print(estudiante)


    # Ejercicio 7 es hacer un listado de 10 diccionarios como el anterior (una fiaca)
EJE4_4to7("Juan", "Gutierrez", 1548, [
          "Matematica", "Fisica", "Quimica", "Ingles"])
