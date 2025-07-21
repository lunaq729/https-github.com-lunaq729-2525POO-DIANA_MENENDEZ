import os
import subprocess  # <<< IMPORTANTE
def run_python_file(filepath):
    print(f"\n--- Ejecutando: {filepath} ---\n")
    try:
        result = subprocess.run(
            [os.sys.executable, filepath],
            capture_output=True,
            text=True,
            check=True
        )
        print(">>> SALIDA:")
        print(result.stdout)
        if result.stderr:
            print(">>> ERRORES (si hay):")
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar {filepath}")
        print(f"Código de retorno: {e.returncode}")
        print("Salida:")
        print(e.stdout)
        print("Errores:")
        print(e.stderr)
    except FileNotFoundError:
        print(f"Archivo no encontrado: {filepath}")
    print("-" * 50)
def main():
    base_dir = r"C:\Users\HOLA\PycharmProjects\2525-POO_Menendez-Diana"

    archivos = {
        '1': 'Parcial 01/SEMANA 2/2.1 Tecnica de Programacion.py',
        '2': 'Parcial 01/SEMANA 3/3.3 Programacion tradicional.py',
        '3': 'Parcial 01/SEMANA 3/3.3 Tarea.py',
        '4': 'Parcial 01/SEMANA 4/5.1 Desarrollo un programa en python.py',
        '5': 'Parcial 01/SEMANA 5/Tarea Semana 05.py',
        '6': 'Parcial 01/SEMANA 6/Clase, Definición de Objeto, Herencia, Encapsulación y Polimorfismo.py',
        '7': 'Parcial 01/SEMANA 7/Implementación de Constructores y Destructores.py'
    }
    while True:
        print("\n===== MENÚ DE EJECUCIÓN DE ARCHIVOS =====")
        for key, path in archivos.items():
            nombre = os.path.basename(path)
            print(f"{key} - {nombre}")

        eleccion = input("Seleccione un archivo para ejecutar (o '0' para salir): ").strip()

        if eleccion == '0':
            print("Saliendo del programa.")
            break
        elif eleccion in archivos:
            ruta_completa = os.path.join(base_dir, archivos[eleccion])
            if os.path.exists(ruta_completa):
                run_python_file(ruta_completa)
            else:
                print(f"Archivo no encontrado: {ruta_completa}")
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()