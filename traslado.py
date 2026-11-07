
import json
import os

# Rutas de los archivos JSON en la misma carpeta del programa
CARPETA = os.path.dirname(os.path.abspath(__file__))

ARCHIVO_ESTUDIANTES = os.path.join(CARPETA, "estudiantes.json")
ARCHIVO_TRASLADOS = os.path.join(CARPETA, "traslados.json")

traslados = []


def cargar_estudiantes():
    if os.path.exists(ARCHIVO_ESTUDIANTES):
        with open(ARCHIVO_ESTUDIANTES, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    return []


def guardar_estudiantes(estudiantes):
    with open(ARCHIVO_ESTUDIANTES, "w", encoding="utf-8") as archivo:
        json.dump(estudiantes, archivo, indent=4, ensure_ascii=False)


def cargar_traslados():
    global traslados

    if os.path.exists(ARCHIVO_TRASLADOS):
        with open(ARCHIVO_TRASLADOS, "r", encoding="utf-8") as archivo:
            traslados = json.load(archivo)
    else:
        traslados = []


def guardar_traslados():
    with open(ARCHIVO_TRASLADOS, "w", encoding="utf-8") as archivo:
        json.dump(traslados, archivo, indent=4, ensure_ascii=False)


def dni_correcto(dni):
    return dni.isdigit() and len(dni) == 8


def buscar_estudiante(dni, estudiantes):
    dni = dni.strip()

    for estudiante in estudiantes:
        dni_guardado = str(estudiante.get("DNI", "")).strip()

        if dni_guardado == dni:
            return estudiante

    return None


def registrar_traslado():
    print("\n--- REGISTRO DE TRASLADO ---")

    estudiantes = cargar_estudiantes()

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados en matricula.")
        print("Primero registre un estudiante en matricula.py.")
        return

    dni = input("Ingrese el DNI del estudiante: ").strip()

    if not dni_correcto(dni):
        print("Error: el DNI debe tener 8 numeros.")
        return

    estudiante = buscar_estudiante(dni, estudiantes)

    if estudiante is None:
        print("Error: estudiante no encontrado.")
        print("Verifique que el DNI este registrado en matricula.")
        return

    if estudiante.get("Estado", "Matriculado") == "Trasladado":
        print("Este estudiante ya tiene el estado Trasladado.")
        return

    print("\n--- DATOS DEL ESTUDIANTE ---")

    for dato, valor in estudiante.items():
        print(f"{dato}: {valor}")

    destino = input("\nIngrese el colegio de destino: ").strip()
    motivo = input("Ingrese el motivo del traslado: ").strip()

    if destino == "" or motivo == "":
        print("Error: debe ingresar el destino y el motivo.")
        return

    confirmacion = input(
        "\n¿Desea confirmar el traslado? (S/N): "
    ).strip().upper()

    if confirmacion != "S":
        print("Traslado cancelado.")
        return

    registro = {
        "DNI": dni,
        "Nombres": estudiante.get("Nombres", ""),
        "Apellidos": estudiante.get("Apellidos", ""),
        "Grado": estudiante.get("Grado", ""),
        "Seccion": estudiante.get("Seccion", ""),
        "Colegio de destino": destino,
        "Motivo": motivo,
        "Estado": "Trasladado"
    }

    traslados.append(registro)

    estudiante["Estado"] = "Trasladado"

    guardar_traslados()
    guardar_estudiantes(estudiantes)

    print("\n¡Traslado registrado correctamente!")


def mostrar_traslados():
    cargar_traslados()

    print("\n--- LISTA DE TRASLADOS ---")

    if len(traslados) == 0:
        print("Todavia no hay traslados registrados.")
        return

    for i, traslado in enumerate(traslados, start=1):
        print(f"\nTraslado {i}")

        for dato, valor in traslado.items():
            print(f"{dato}: {valor}")


def buscar_traslado():
    cargar_traslados()

    print("\n--- BUSCAR TRASLADO ---")

    dni = input("Ingrese el DNI del estudiante: ").strip()

    if not dni_correcto(dni):
        print("Error: el DNI debe tener 8 numeros.")
        return

    encontrado = False

    for traslado in traslados:
        if str(traslado.get("DNI", "")).strip() == dni:
            print("\n--- DATOS DEL TRASLADO ---")

            for dato, valor in traslado.items():
                print(f"{dato}: {valor}")

            encontrado = True

    if not encontrado:
        print("No se encontraron traslados para este DNI.")


def menu():
    cargar_traslados()

    while True:
        print("\n===== SISTEMA DE TRASLADOS =====")
        print("1. Registrar traslado")
        print("2. Mostrar traslados")
        print("3. Buscar traslado por DNI")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_traslado()

        elif opcion == "2":
            mostrar_traslados()

        elif opcion == "3":
            buscar_traslado()

        elif opcion == "0":
            print("Saliendo del sistema de traslados...")
            break

        else:
            print("Opcion incorrecta. Intente nuevamente.")


if __name__ == "__main__":
    menu()

