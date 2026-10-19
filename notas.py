
notas = [] 


def dni_correcto(dni):
    return dni.isdigit() and len(dni) == 8


def bimestre_valido(bimestre):
    return bimestre in["1","2","3","4"]


def nota_valida(nota):
    if not nota.isdigit():
        return False
    return 0 <= int(nota) <= 20

def nota_repetida(dni, curso, bimestre):
    for n in notas:
        if n["dni"]==dni and n["curso"].lower()==curso.lower() and n["bimestre"]==bimestre:
            return True
        return False

def registrar_nota():
    print("--- REGISTRAR NOTA ---")
    dni = input("DNI del estudiante: ")
    curso = input("Curso (Matemática, Comunicación, etc.): ")
    bimestre = input("Bimestre (1 a 4): ")
    nota = input("Nota (0 a 20): ")

    if not dni_correcto(dni):
        print("El DNI debe tener 8 números.")
    elif curso == "":
        print("Debe ingresar el curso.")
    elif not bimestre_valido(bimestre):
        print("El bimestre debe ser 1, 2, 3 o 4.")
    elif not nota_valida(nota):
        print("La nota debe ser un número entre 0 y 20.")
    elif nota_repetida(dni, curso, bimestre):
        print("Error:Ya exite una nota de ese curso y bimestre para este estudiante.")
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
 # COMMIT 4: MENÚ PRINCIPAL
def menu_principal():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Registrar estudiante")
        print("2. Buscar estudiante por DNI")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            buscar_estudiante()
        elif opcion == "0":
            print("Hasta pronto.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu_principal()