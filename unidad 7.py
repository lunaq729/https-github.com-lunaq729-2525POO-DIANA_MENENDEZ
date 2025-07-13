class Archivo:
    """
    Clase que simula la apertura y cierre de un archivo.
    """

    def __init__(self, nombre):
        """
        Constructor: se llama automáticamente al crear un objeto.
        Inicializa el nombre del archivo y simula abrirlo.
        """
        self.nombre = nombre
        self.abierto = True
        print(f"Archivo '{self.nombre}' abierto.")

    def escribir(self, contenido):
        """
        Método para simular la escritura en el archivo.
        """
        if self.abierto:
            print(f"Escribiendo en '{self.nombre}': {contenido}")
        else:
            print(f"No se puede escribir, el archivo '{self.nombre}' está cerrado.")

    def __del__(self):
        """
        Destructor: se llama automáticamente cuando el objeto es destruido.
        Simula el cierre del archivo para liberar recursos.
        """
        if self.abierto:
            self.abierto = False
            print(f"Archivo '{self.nombre}' cerrado y recursos liberados.")

# Uso del programa
def main():
    # Crear un objeto Archivo (se llama __init__)
    archivo1 = Archivo("datos.txt")
    archivo1.escribir("Programacion de objeto!")

    # Eliminar el objeto para forzar llamada al destructor (__del__)
    del archivo1

if __name__ == "__main__":
    main()

PS C:\Users\Personal\Downloads\PARCIAL 01\UNIDAD 7\DEBER 7> & C:/Users/Personal/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/Personal/Downloads/PARCIAL 01/DEBER 7/unudad 7.py"
Archivo 'datos.txt' abierto.
Escribiendo en 'datos.txt': Programacion de objeto!
Archivo 'datos.txt' cerrado y recursos liberados.
PS C:\Users\Personal\Downloads\PARCIAL 01\UNIDAD 7\DEBER 7>

