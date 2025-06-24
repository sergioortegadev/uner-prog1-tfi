import sys
from controller import controller_users as usuarios
from controller import controller_tools as herramientas
from controller import controller_loans as asignaciones
from controller import controller_maintenance as mantenimientos

# ======== FUNCIONES DE VALIDACIÓN ========

def validar_opcion(mensaje, opciones_validas):
    while True:
        opcion = input(mensaje).strip()
        if opcion in opciones_validas:
            return opcion
        print("Opción inválida. Intente nuevamente.")

def validar_dni(mensaje="Ingrese DNI: "):
    while True:
        dni = input(mensaje).strip()
        if dni.isdigit() and 7 <= len(dni) <= 8:
            return int(dni)
        print("DNI inválido. Debe ser numérico y tener 7 u 8 dígitos.")

def validar_id(mensaje="Ingrese ID: "):
    while True:
        id_input = input(mensaje).strip()
        if id_input.isdigit():
            return int(id_input)
        print("ID inválido. Debe ser numérico.")

def validar_fecha(mensaje="Ingrese fecha (YYYY-MM-DD): "):
    import datetime
    while True:
        fecha = input(mensaje).strip()
        try:
            datetime.datetime.strptime(fecha, "%Y-%m-%d")
            return fecha
        except ValueError:
            print("Fecha inválida. Use el formato YYYY-MM-DD.")

# ======== MENÚ PRINCIPAL ========

def menu():
    while True:
        print("\n=== Menú Principal ===")
        print("1 - Asignaciones")
        print("2 - Usuarios")
        print("3 - Herramientas")
        print("4 - Mantenimiento")
        print("0 - Salir")

        opcion = validar_opcion("Seleccione una opción: ", ["1", "2", "3", "4", "0"])

        if opcion == "1":
            menu_asignaciones()
        elif opcion == "2":
            menu_usuarios()
        elif opcion == "3":
            menu_herramientas()
        elif opcion == "4":
            menu_mantenimiento()
        elif opcion == "0":
            print("Gracias por usar el sistema.")
            sys.exit(0)

# ======== SUBMENÚS ========

def imprimir_resultado(result):
    print(f"\n{result['message']}")
    print(result["to_print"])

def menu_asignaciones():
    while True:
        print("\n--- Menú Asignaciones ---")
        print("1 - Registrar préstamo")
        print("2 - Registrar devolución")
        print("3 - Ver historial por usuario")
        print("4 - Ver historial por herramienta")
        print("5 - Ver listado completo")
        print("0 - Volver")

        opcion = validar_opcion("Seleccione una opción: ", ["1", "2", "3", "4", "5", "0"])

        match opcion:
            case "1":
                id_tool = validar_id("ID herramienta: ")
                dni = validar_dni("DNI usuario: ")
                imprimir_resultado(asignaciones.loan_create(id_tool, dni))
            case "2":
                id_tool = validar_id("ID herramienta: ")
                dni = validar_dni("DNI usuario: ")
                obs = input("Observaciones: ")
                imprimir_resultado(asignaciones.loan_return(id_tool, dni, obs))
            case "3":
                dni = validar_dni()
                imprimir_resultado(asignaciones.loan_get_user(dni))
            case "4":
                id_tool = validar_id()
                imprimir_resultado(asignaciones.loan_get_tool(id_tool))
            case "5":
                imprimir_resultado(asignaciones.loan_list())
            case "0":
                return

def menu_usuarios():
    while True:
        print("\n--- Menú Usuarios ---")
        print("1 - Crear usuario")
        print("2 - Editar usuario")
        print("3 - Eliminar usuario")
        print("4 - Buscar por DNI")
        print("5 - Buscar por nombre")
        print("6 - Listar todos")
        print("7 - Listar por tipo")
        print("0 - Volver")

        opcion = validar_opcion("Seleccione una opción: ", [str(i) for i in range(8)])

        match opcion:
            case "1":
                dni = validar_dni()
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                email = input("Email: ")
                tipo = input("Tipo (Estudiante/Personal): ")
                curso = input("Curso (si aplica): ")
                taller = input("Taller (si aplica): ")
                rol = input("Rol (si aplica): ")
                dep = input("Departamento (si aplica): ")
                imprimir_resultado(usuarios.user_create(dni, nombre, apellido, email, tipo, curso, taller, rol, dep))
            case "2":
                dni = validar_dni()
                imprimir_resultado(usuarios.user_update(dni))
            case "3":
                dni = validar_dni()
                imprimir_resultado(usuarios.user_delete(dni))
            case "4":
                dni = validar_dni()
                imprimir_resultado(usuarios.user_get_by_dni(dni))
            case "5":
                nombre = input("Nombre: ")
                imprimir_resultado(usuarios.user_get_by_name(nombre))
            case "6":
                imprimir_resultado(usuarios.users_list())
            case "7":
                tipo = input("Tipo (Estudiante/Personal): ")
                imprimir_resultado(usuarios.users_list_by_type(tipo))
            case "0":
                return

def menu_herramientas():
    while True:
        print("\n--- Menú Herramientas ---")
        print("1 - Crear herramienta")
        print("2 - Editar herramienta")
        print("3 - Eliminar herramienta")
        print("4 - Buscar por ID")
        print("5 - Buscar por nombre")
        print("6 - Listar todas")
        print("7 - Listar por tipo")
        print("0 - Volver")

        opcion = validar_opcion("Seleccione una opción: ", [str(i) for i in range(8)])

        match opcion:
            case "1":
                name = input("Nombre: ")
                tipo = input("Tipo: ")
                marca = input("Marca: ")
                modelo = input("Modelo: ")
                estado = input("Estado: ")
                ubicacion = input("Ubicación: ")
                observaciones = input("Observaciones: ")
                disponible = input("¿Disponible? (s/n): ").lower() == "s"
                imprimir_resultado(herramientas.tool_create(name, tipo, marca, modelo, estado, ubicacion, observaciones, disponible))
            case "2":
                id_tool = validar_id()
                imprimir_resultado(herramientas.tool_update(id_tool))
            case "3":
                id_tool = validar_id()
                imprimir_resultado(herramientas.tool_delete(id_tool))
            case "4":
                id_tool = validar_id()
                imprimir_resultado(herramientas.tool_get_by_id(id_tool))
            case "5":
                name = input("Nombre: ")
                imprimir_resultado(herramientas.tool_get_by_name(name))
            case "6":
                imprimir_resultado(herramientas.tools_list_all())
            case "7":
                tipo = input("Tipo: ")
                imprimir_resultado(herramientas.tools_list_by_type(tipo))
            case "0":
                return

def menu_mantenimiento():
    while True:
        print("\n--- Menú Mantenimiento ---")
        print("1 - Registrar mantenimiento")
        print("2 - Ver historial completo")
        print("0 - Volver")

        opcion = validar_opcion("Seleccione una opción: ", ["1", "2", "0"])

        match opcion:
            case "1":
                id_tool = validar_id()
                fecha = validar_fecha()
                tipo = input("Tipo (Preventivo/Correctivo): ")
                descripcion = input("Descripción: ")
                responsable = input("Responsable: ")
                costo = input("Costo: ")
                siguiente = input("Próximo (YYYY-MM-DD o N/A): ")
                imprimir_resultado(mantenimientos.maintenance_create(id_tool, fecha, tipo, descripcion, responsable, costo, siguiente))
            case "2":
                imprimir_resultado(mantenimientos.maintenance_list_all())
            case "0":
                return
