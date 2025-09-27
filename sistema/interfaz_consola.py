# interfaz_consola.py actualizado para guardar después de agregar instructor o cliente

from datetime import date
from modelos.sucursal import Sucursal
from modelos.instructor import Instructor
from modelos.cliente import Cliente
from modelos.enums import Especialidad
from sistema.persistencia import guardar_datos

class InterfazConsola:
    def __init__(self, sistema):
        self.sistema = sistema

    def mostrar_menu_principal(self):
        print("\n=== SISTEMA DE GESTIÓN POWERLAB ===")
        print("1. Gestión de Sucursales")
        print("2. Gestión de Instructores")
        print("3. Gestión de Clientes")
        print("0. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu_principal()
            opcion = input("\nSeleccione una opción: ")

            if opcion == "1":
                self.menu_sucursales()
            elif opcion == "2":
                self.menu_instructores()
            elif opcion == "3":
                self.menu_clientes()
            elif opcion == "0":
                print("Gracias por usar PowerLab")
                break
            else:
                print("Opción inválida")

    # ----------------------------
    # SUCURSALES
    # ----------------------------
    def menu_sucursales(self):
        print("\n--- Gestión de Sucursales ---")
        print("1. Agregar Sucursal")
        print("2. Listar Sucursales")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Código: ")
            provincia = input("Provincia: ")
            canton = input("Cantón: ")
            correo = input("Correo: ")
            telefono = input("Teléfono: ")
            sucursal = Sucursal(codigo, provincia, canton, correo, telefono)
            if self.sistema.agregar_sucursal(sucursal):
                guardar_datos(self.sistema)
                print("Sucursal agregada correctamente.")
            else:
                print("No se pudo agregar (límite alcanzado).")
        elif opcion == "2":
            for suc in self.sistema.sucursales:
                print(f"- {suc.codigo} | {suc.provincia}, {suc.canton}")
        elif opcion == "0":
            return
        else:
            print("Opción inválida")

    # ----------------------------
    # INSTRUCTORES
    # ----------------------------
    def menu_instructores(self):
        print("\n--- Gestión de Instructores ---")
        print("1. Agregar Instructor a una Sucursal")
        print("2. Listar Instructores")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            suc_codigo = input("Código de la sucursal: ")
            suc = self.sistema.buscar_sucursal(suc_codigo)
            if suc:
                cedula = input("Cédula: ")
                nombre = input("Nombre completo: ")
                telefono = input("Teléfono: ")
                correo = input("Correo: ")
                nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
                fecha_nac = date.fromisoformat(nacimiento)

                instructor = Instructor(cedula, nombre, telefono, correo, fecha_nac)

                # Agregar especialidades
                print("Especialidades disponibles:")
                for esp in Especialidad:
                    print(f"- {esp.value}")
                while True:
                    esp = input("Ingrese una especialidad (ENTER para terminar): ")
                    if not esp:
                        break
                    try:
                        instructor.agregar_especialidad(Especialidad[esp.upper()])
                    except KeyError:
                        print("Especialidad inválida.")

                suc.agregar_instructor(instructor)
                guardar_datos(self.sistema)  # Guarda inmediatamente
                print("Instructor agregado correctamente.")
            else:
                print("Sucursal no encontrada.")
        elif opcion == "2":
            for suc in self.sistema.sucursales:
                print(f"\nSucursal {suc.codigo}:")
                for ins in suc.instructores:
                    print(f"- {ins.nombre_completo} ({ins.cedula})")
        elif opcion == "0":
            return
        else:
            print("Opción inválida")

    # ----------------------------
    # CLIENTES
    # ----------------------------
    def menu_clientes(self):
        print("\n--- Gestión de Clientes ---")
        print("1. Registrar Cliente en una Sucursal")
        print("2. Listar Clientes")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            suc_codigo = input("Código de la sucursal: ")
            suc = self.sistema.buscar_sucursal(suc_codigo)
            if suc:
                if not suc.instructores:
                    print("Sucursal sin instructores. No se puede registrar cliente sin asignar un instructor.")
                    return

                cedula = input("Cédula: ")
                nombre = input("Nombre completo: ")
                telefono = input("Teléfono: ")
                correo = input("Correo: ")
                nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
                fecha_nac = date.fromisoformat(nacimiento)
                sexo = input("Sexo (M/F): ").upper()
                fecha_insc = date.today()

                cliente = Cliente(cedula, nombre, telefono, correo, fecha_nac, sexo, fecha_insc)

                # Asignar instructor (obligatorio ya que hay instructores)
                print("\nInstructores disponibles:")
                for idx, ins in enumerate(suc.instructores, start=1):
                    print(f"{idx}. {ins.nombre_completo}")
                try:
                    opc = int(input("Seleccione instructor: ")) - 1
                    if 0 <= opc < len(suc.instructores):
                        cliente.asignar_instructor(suc.instructores[opc])
                    else:
                        print("Selección inválida. Registro cancelado.")
                        return
                except ValueError:
                    print("Entrada inválida. Registro cancelado.")
                    return

                suc.agregar_cliente(cliente)
                guardar_datos(self.sistema)  # Guarda inmediatamente
                print("Cliente registrado correctamente.")
            else:
                print("Sucursal no encontrada.")
        elif opcion == "2":
            for suc in self.sistema.sucursales:
                print(f"\nSucursal {suc.codigo}:")
                for cli in suc.clientes:
                    print(f"- {cli.nombre_completo} ({cli.cedula})")
        elif opcion == "0":
            return
        else:
            print("Opción inválida")