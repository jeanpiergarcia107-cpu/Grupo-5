
import json
import os

ARCHIVO_ESTUDIANTES = "estudiantes.json"


def cargar_estudiantes():
    if os.path.exists(ARCHIVO_ESTUDIANTES):
        with open(ARCHIVO_ESTUDIANTES, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    return []


def guardar_estudiantes():
    with open(ARCHIVO_ESTUDIANTES, "w", encoding="utf-8") as archivo:
        json.dump(estudiantes, archivo, indent=4, ensure_ascii=False)


estudiantes = cargar_estudiantes()


def registrar_estudiante():
    print("\n--- REGISTRO DE MATRICULA ---")

    dni = input("Ingrese el DNI: ").strip()

    if not dni.isdigit() or len(dni) != 8:
        print("Error: el DNI debe tener 8 numeros.")
        return

    # Verificar si el DNI ya esta registrado
    for estudiante in estudiantes:
        if estudiante["DNI"] == dni:
            print("Error: este estudiante ya esta registrado.")
            return

    nombres = input("Ingrese los nombres: ")
    apellidos = input("Ingrese los apellidos: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento: ")
    grado = input("Ingrese el grado: ")
    seccion = input("Ingrese la seccion: ")
    anio = input("Ingrese el año academico: ")
    apoderado = input("Ingrese el nombre del apoderado: ")
    telefono = input("Ingrese el telefono del apoderado: ")

    estudiante = {
        "DNI": dni,
        "Nombres": nombres,
        "Apellidos": apellidos,
        "Fecha de nacimiento": fecha_nacimiento,
        "Grado": grado,
        "Seccion": seccion,
        "Año academico": anio,
        "Apoderado": apoderado,
        "Telefono": telefono,
        "Estado": "Matriculado"
    }

    estudiantes.append(estudiante)
    guardar_estudiantes()

    print("\n¡Matricula registrada correctamente!")


def listar_estudiantes():
    print("\n--- LISTA DE ESTUDIANTES ---")

    if len(estudiantes) == 0:
        print("Todavia no hay estudiantes registrados.")
    else:
        for i, estudiante in enumerate(estudiantes, start=1):
            print(f"\nEstudiante {i}")

            for dato, valor in estudiante.items():
                print(f"{dato}: {valor}")


def menu():
    while True:
        print("\n===== SISTEMA DE MATRICULA =====")
        print("1. Registrar estudiante")
        print("2. Listar estudiantes")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_estudiante()

        elif opcion == "2":
            listar_estudiantes()

        elif opcion == "0":
            print("Saliendo del sistema de matricula...")
            break

        else:
            print("Opcion incorrecta. Intente nuevamente.")


if __name__ == "__main__":
    menu()
