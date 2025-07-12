# Clase Libro para representar un libro en la biblioteca
class Libro:
    def __init__(self, titulo, autor):
        # Constructor: se ejecuta automáticamente al crear un objeto de la clase
        self.titulo = titulo
        self.autor = autor
        print(f"📘 Se ha creado el libro: '{self.titulo}' por {self.autor}")

    def mostrar_info(self):
        # Método para mostrar información del libro
        print(f"Título: {self.titulo}, Autor: {self.autor}")

    def __del__(self):
        # Destructor: se ejecuta automáticamente cuando el objeto se elimina o el programa termina
        print(f"🗑️ El libro '{self.titulo}' ha sido eliminado de la memoria.")


# Programa principal
def main():
    print("📚 Bienvenido al sistema de gestión de libros")

    # Crear algunos libros
    libro1 = Libro("El amor las mujeres y la vida", "Mario Benedetti")
    libro2 = Libro("Tierra de Hombres", "Antoine de Saint-Exupéry")

    # Mostrar información
    libro1.mostrar_info()
    libro2.mostrar_info()

    # Eliminar manualmente un objeto (para ver cuándo se activa el destructor)
    del libro1

    print("✅ Fin del programa")




