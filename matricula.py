# PRIMER COMMIT: REGISTRO DE MATRICULA
# Proyecto: Sistema de matricula de estudiantes

estudiantes = []

def registrar_estudiante():
    print("\n--- REGISTRO DE MATRICULA ---")
    
    dni = input("Ingrese el DNI: ")
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
        "Telefono": telefono
    }
    
    estudiantes.append(estudiante)
    
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

registrar_estudiante()
listar_estudiantes()