import sys
import view.style
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
        if dni == "0":
         return None
        if dni.isdigit() and 7 <= len(dni) <= 8:
            return int(dni)
        print("DNI inválido. Debe ser numérico y tener 7 u 8 dígitos.")

def validar_id(mensaje="Ingrese ID: "):
    while True:
        id_input = input(mensaje).strip()
        if id_input == "0":
            return None
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

# ======== FUNCIONES DE IMPRESIÓN ========
def imprimir_resultado(result):
    view.style.normal_cyan(f"\n{result['message']}\n")

    to_print = result.get("to_print", {})
    for each in to_print:
        if isinstance(each, dict):
            # print(f"{each.get('id', 'Desconocido')}:")
            for key, value in each.items():
                print(f"  - {key}: {value}")
            print("\n")
        else:
            print(f"{each.capitalize()}: {to_print[each]}")

# ======== FUNCIONES DE INTERACCIÓN CON EL USUARIO ========
def _obtener_datos_usuario():
    """Solicita y retorna un diccionario con los datos de un usuario."""
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = input("Email: ")
    while True:
        tipo = input("Tipo (Estudiante/Personal): ").lower()
        if tipo in ["estudiante", "personal"]:
            break
        print("Tipo inválido. Debe ser 'Estudiante' o 'Personal'.")

    datos_usuario = {
        "first_name": nombre,
        "last_name": apellido,
        "email": email,
        "user_type": tipo.capitalize(),
        "curso": "",
        "taller": "",
        "role": "",
        "dep": ""
    }

    if tipo == "estudiante":
        datos_usuario["curso"] = input("Curso (si aplica): ")
        datos_usuario["taller"] = input("Taller (si aplica): ")
    elif tipo == "personal":
        datos_usuario["role"] = input("Rol (si aplica): ")
        datos_usuario["dep"] = input("Departamento (si aplica): ")
    
    return datos_usuario            

def _obtener_datos_herramienta():
    """Solicita y retorna un diccionario con los datos de una herramienta."""
    nombre = input("Nombre: ")
    tipo = input("Tipo: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    estado = input("Estado: ")
    ubicacion = input("Ubicación (S01-E01-R01): ")
    observaciones = input("Observaciones: ")

    return {
        "nombre": nombre,
        "tipo": tipo,
        "marca": marca,
        "modelo": modelo,
        "estado": estado,
        "ubicacion": ubicacion,
        "observaciones": observaciones
    }

# ======== MENÚ PRINCIPAL ========

def menu():
    while True:
        view.style.header("\n   === Menú Principal ===")
        print("   1 - Asignaciones")
        print("   2 - Usuarios")
        print("   3 - Herramientas")
        print("   4 - Mantenimiento")
        print("   0 - Salir\n")

        opcion = validar_opcion("   Seleccione una opción: ", ["1", "2", "3", "4", "0"])

        if opcion == "1":
            menu_asignaciones()
        elif opcion == "2":
            menu_usuarios()
        elif opcion == "3":
            menu_herramientas()
        elif opcion == "4":
            menu_mantenimiento()
        elif opcion == "0":
            view.style.header("\n\n   Gracias por usar el sistema.")
            view.style.footer()
            sys.exit(0)

# ======== SUBMENÚS ========



def menu_asignaciones():
    while True:
        view.style.subheader("\n   --- Menú Asignaciones ---")
        print("   1 - Registrar préstamo")
        print("   2 - Registrar devolución")
        print("   3 - Ver historial por usuario")
        print("   4 - Ver historial por herramienta")
        print("   5 - Ver listado completo")
        print("   0 - Volver")

        opcion = validar_opcion("\n   Seleccione una opción: ", ["1", "2", "3", "4", "5", "0"])

        match opcion:
            case "1":
                id_tool = validar_id("ID herramienta: ")
                if id_tool is None:
                    print("Operación cancelada.")
                    return
                dni = validar_dni("DNI usuario: ")
                imprimir_resultado(asignaciones.loan_create(id_tool, dni))
            case "2":
                id_tool = validar_id("ID herramienta: ")
                obs = input("Observaciones: ")
                imprimir_resultado(asignaciones.loan_return(id_tool, obs))
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
        view.style.subheader("\n   --- Menú Usuarios ---")
        print("   1 - Crear usuario")
        print("   2 - Editar usuario")
        print("   3 - Eliminar usuario")
        print("   4 - Buscar por DNI")
        print("   5 - Buscar por nombre")
        print("   6 - Listar todos")
        print("   7 - Listar por tipo")
        print("   0 - Volver")

        opcion = validar_opcion("\n   Seleccione una opción: ", [str(i) for i in range(8)])

        match opcion:
            case "1":
                dni = validar_dni()
                datos = _obtener_datos_usuario()
                usuarios.user_create(dni, **datos)
                #imprimir_resultado(usuarios.user_create(dni, **datos))
             
            case "2":
                dni = validar_dni()
                datos = _obtener_datos_usuario()
                imprimir_resultado(usuarios.user_update(dni, **datos))
            case "3":
                dni = validar_dni()
                if dni is None:
                    print("Operación cancelada.")
                    return
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
        view.style.subheader("\n   --- Menú Herramientas ---")
        print("   1 - Listar todas las herramientas")
        print("   2 - Buscar por ID")
        print("   3 - Buscar por nombre")
        print("   4 - Crear herramienta")
        print("   5 - Editar herramienta")
        print("   6 - Eliminar herramienta")
        # print("   7 - Listar por tipo") # No implementado en el JSON
        print("   0 - Volver")

        opcion = validar_opcion("\n   Seleccione una opción: ", [str(i) for i in range(8)])

        match opcion:
            case "1":
                imprimir_resultado(herramientas.tools_list_all())
            case "2":
                id_tool = validar_id()
                imprimir_resultado(herramientas.tool_get_by_id(id_tool))
            case "3":
                name = input("Nombre: ")
                imprimir_resultado(herramientas.tool_get_by_name(name))
            case "4":
                datos_herramienta = _obtener_datos_herramienta()
                imprimir_resultado(herramientas.tool_create(**datos_herramienta))
            case "5":
                id_tool = validar_id()
                imprimir_resultado(herramientas.tool_update(id_tool))
            case "6":
                id_tool = validar_id()
                imprimir_resultado(herramientas.tool_delete(id_tool))
            # case "7":
            #     tipo = input("Tipo: ")
            #     imprimir_resultado(herramientas.tools_list_by_type(tipo))
            case "0":
                return

def menu_mantenimiento():
    while True:
        view.style.subheader("\n   --- Menú Mantenimiento ---")
        print("   1 - Registrar mantenimiento")
        print("   2 - Ver historial completo")
        print("   0 - Volver")

        opcion = validar_opcion("\n   Seleccione una opción: ", ["1", "2", "0"])

        match opcion:
            case "1":
                id_tool = validar_id()
                if id_tool is None:
                    print("Operación cancelada.")
                    return
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
