
# MODULO DE TRASLADO DE ESTUDIANTES
# Proyecto: Sistema de gestion escolar - Grupo 5

import json
import os

# DATOS DE ESTUDIANTES
estudiantes = [
    {
        "DNI": "12345678",
        "Nombres": "Ana",
        "Apellidos": "Perez",
        "Grado": "3",
        "Seccion": "A",
        "Estado": "Matriculado"
    },
    {
        "DNI": "87654321",
        "Nombres": "Carlos",
        "Apellidos": "Lopez",
        "Grado": "4",
        "Seccion": "B",
        "Estado": "Matriculado"
    },
    {
        "DNI": "11223344",
        "Nombres": "Maria",
        "Apellidos": "Gomez",
        "Grado": "5",
        "Seccion": "A",
        "Estado": "Matriculado"
    }
]

ARCHIVO_TRASLADOS = "traslados.json"

traslados = []


# VALIDAR DNI
def dni_correcto(dni):

    return dni.isdigit() and len(dni) == 8


# BUSCAR ESTUDIANTE
def buscar_estudiante(dni):

    for estudiante in estudiantes:

        if estudiante["DNI"] == dni:

            return estudiante

    return None


# CARGAR TRASLADOS
def cargar_traslados():

    global traslados

    if os.path.exists(ARCHIVO_TRASLADOS):

        try:

            with open(
                ARCHIVO_TRASLADOS,
                "r",
                encoding="utf-8"
            ) as archivo:

                traslados = json.load(archivo)

        except (json.JSONDecodeError, OSError):

            traslados = []

    else:

        traslados = []


# GUARDAR TRASLADOS
def guardar_traslados():

    try:

        with open(
            ARCHIVO_TRASLADOS,
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                traslados,
                archivo,
                ensure_ascii=False,
                indent=4
            )

        return True

    except OSError:

        print("Error al guardar el archivo.")

        return False


# REGISTRAR TRASLADO
def registrar_traslado():

    print("\n===== REGISTRO DE TRASLADO =====")

    dni = input("Ingrese el DNI del estudiante: ").strip()

    if not dni_correcto(dni):

        print("Error: El DNI debe tener 8 numeros.")

        return

    estudiante = buscar_estudiante(dni)

    if estudiante is None:

        print("Estudiante no encontrado.")

        return

    if estudiante["Estado"] == "Trasladado":

        print("El estudiante ya fue trasladado.")

        return

    # MOSTRAR DATOS DEL ESTUDIANTE
    print("\n===== DATOS DEL ESTUDIANTE =====")

    print("DNI:", estudiante["DNI"])
    print("Nombres:", estudiante["Nombres"])
    print("Apellidos:", estudiante["Apellidos"])
    print("Grado:", estudiante["Grado"])
    print("Seccion:", estudiante["Seccion"])
    print("Estado:", estudiante["Estado"])

    # INGRESAR DATOS DEL TRASLADO
    destino = input(
        "\nIngrese el colegio de destino: "
    ).strip()

    if destino == "":

        print("Debe ingresar el colegio de destino.")

        return

    motivo = input(
        "Ingrese el motivo del traslado: "
    ).strip()

    if motivo == "":

        print("Debe ingresar el motivo.")

        return

    confirmar = input(
        "¿Confirmar traslado? (S/N): "
    ).strip().upper()

    if confirmar != "S":

        print("Registro cancelado.")

        return

    # CREAR REGISTRO
    registro = {

        "DNI": estudiante["DNI"],

        "Nombres": estudiante["Nombres"],

        "Apellidos": estudiante["Apellidos"],

        "Grado": estudiante["Grado"],

        "Seccion": estudiante["Seccion"],

        "Colegio destino": destino,

        "Motivo": motivo,

        "Estado": "Trasladado"
    }

    traslados.append(registro)

    if guardar_traslados():

        estudiante["Estado"] = "Trasladado"

        print("\n¡TRASLADO REGISTRADO CORRECTAMENTE!")

        print("Estudiante:", estudiante["Nombres"])

        print("Colegio destino:", destino)

        print("Estado: Trasladado")

    else:

        traslados.pop()

        print("No se pudo guardar el traslado.")


# MOSTRAR TRASLADOS
def mostrar_traslados():

    print("\n===== LISTA DE TRASLADOS =====")

    if len(traslados) == 0:

        print("No hay traslados registrados.")

        return

    for i, traslado in enumerate(
        traslados,
        start=1
    ):

        print("\nTraslado", i)

        for dato, valor in traslado.items():

            print(dato + ":", valor)


# BUSCAR TRASLADO
def buscar_traslado():

    print("\n===== BUSCAR TRASLADO =====")

    dni = input("Ingrese el DNI: ").strip()

    if not dni_correcto(dni):

        print("El DNI debe tener 8 numeros.")

        return

    encontrado = False

    for traslado in traslados:

        if traslado["DNI"] == dni:

            print("\n===== CONSTANCIA DE TRASLADO =====")

            for dato, valor in traslado.items():

                print(dato + ":", valor)

            encontrado = True

    if not encontrado:

        print("No se encontro el traslado.")


# MENU PRINCIPAL
def menu():

    cargar_traslados()

    opcion = ""

    while opcion != "0":

        print("\n===== MODULO DE TRASLADO =====")

        print("1. Registrar traslado")

        print("2. Mostrar traslados")

        print("3. Buscar traslado por DNI")

        print("0. Salir")

        opcion = input(
            "Seleccione una opcion: "
        ).strip()

        if opcion == "1":

            registrar_traslado()

        elif opcion == "2":

            mostrar_traslados()

        elif opcion == "3":

            buscar_traslado()

        elif opcion == "0":

            print("Saliendo del modulo de traslado.")

        else:

            print("Opcion no valida.")


# EJECUTAR PROGRAMA
if __name__ == "__main__":

    menu()
