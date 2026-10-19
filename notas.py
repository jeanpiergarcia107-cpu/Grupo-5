
notas = []   # aquí se guardan todas las notas


def dni_correcto(dni):
    # el DNI debe tener 8 números
    return dni.isdigit() and len(dni) == 8


def bimestre_valido(bimestre):
    return bimestre == "1" or bimestre == "2" or bimestre == "3" or bimestre == "4"


def nota_valida(nota):
    # la nota debe ser un número entero entre 0 y 20
    if nota.isdigit() == False:
        return False
    return int(nota) >= 0 and int(nota) <= 20


def registrar_nota():
    print("--- REGISTRAR NOTA ---")
    dni = input("DNI del estudiante: ")
    curso = input("Curso (Matemática, Comunicación, etc.): ")
    bimestre = input("Bimestre (1 a 4): ")
    nota = input("Nota (0 a 20): ")

    if dni_correcto(dni) == False:
        print("El DNI debe tener 8 números.")
    elif curso == "":
        print("Debe ingresar el curso.")
    elif bimestre_valido(bimestre) == False:
        print("El bimestre debe ser 1, 2, 3 o 4.")
    elif nota_valida(nota) == False:
        print("La nota debe ser un número entre 0 y 20.")
    else:
        registro = {
            "dni": dni,
            "curso": curso,
            "bimestre": bimestre,
            "nota": int(nota)
        }
        notas.append(registro)
        print("Nota registrada correctamente.")


def mostrar_notas():
    print("--- NOTAS DE UN ESTUDIANTE ---")
    dni = input("DNI del estudiante: ")
    encontro = False
    for n in notas:
        if n["dni"] == dni:
            print("Curso:", n["curso"], "| Bimestre:", n["bimestre"], "| Nota:", n["nota"])
            encontro = True
    if encontro == False:
        print("Ese estudiante no tiene notas registradas.")


# Menú de prueba (solo se usa si ejecutan este archivo solo)
if __name__ == "__main__":
    opcion = ""
    while opcion != "0":
        print("\n===== MÓDULO DE NOTAS =====")
        print("1. Registrar nota")
        print("2. Ver notas de un estudiante")
        print("0. Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            registrar_nota()
        elif opcion == "2":
            mostrar_notas()
        elif opcion == "0":
            print("Hasta pronto.")
        else:
            print("Opción no válida.")