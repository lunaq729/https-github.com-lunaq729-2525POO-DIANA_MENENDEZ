"""
Este programa demuestra los conceptos fundamentales de la Programación Orientada a Objetos:
- Herencia
- Encapsulación
- Polimorfismo
"""

# Clase base que representa un vehículo genérico
class Vehiculo:
    def __init__(self, marca, modelo, año):
        """
        Constructor de la clase base Vehiculo
        :param marca: str - marca del vehículo
        :param modelo: str - modelo del vehículo
        :param año: int - año de fabricación
        """
        self._marca = marca  # Atributo protegido (encapsulación)
        self._modelo = modelo
        self._año = año
        self._kilometraje = 0  # Atributo interno protegido

    def describir(self):
        """Método que describe el vehículo"""
        return f"{self._marca} {self._modelo} del año {self._año}"

    def avanzar(self, kilometros):
        """
        Método para incrementar el kilometraje
        :param kilometros: int - kilómetros a añadir
        """
        if kilometros > 0:
            self._kilometraje += kilometros
        else:
            print("Los kilómetros deben ser positivos")

    # Getter para kilometraje (encapsulación)
    def get_kilometraje(self):
        return self._kilometraje

    # Método que será sobrescrito (polimorfismo)
    def tipo_vehiculo(self):
        return "Vehículo genérico"


# Clase derivada que hereda de Vehiculo
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, num_puertas):
        """
        Constructor de la clase derivada Automovil
        :param num_puertas: int - número de puertas
        """
        super().__init__(marca, modelo, año)  # Llamada al constructor de la clase base
        self.__num_puertas = num_puertas  # Atributo privado (encapsulación fuerte)

    # Sobrescritura del método (polimorfismo)
    def tipo_vehiculo(self):
        return "Automóvil"

    # Método específico de Automovil
    def abrir_puertas(self):
        print(f"Abriendo {self.__num_puertas} puertas del {self._marca}")

    # Getter para num_puertas (encapsulación)
    def get_num_puertas(self):
        return self.__num_puertas


# Otra clase derivada que hereda de Vehiculo
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        """
        Constructor de la clase derivada Motocicleta
        :param cilindrada: int - cilindrada en cc
        """
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada

    # Sobrescritura del método (polimorfismo)
    def tipo_vehiculo(self):
        return "Motocicleta"

    # Método específico de Motocicleta
    def hacer_caballito(self):
        print(f"La {self._marca} {self._modelo} está haciendo un caballito!")


# Función que demuestra polimorfismo
def mostrar_tipo(vehiculo):
    """
    Función que acepta cualquier objeto Vehiculo y muestra su tipo
    :param vehiculo: Objeto de tipo Vehiculo o sus derivados
    """
    print(f"Este es un {vehiculo.tipo_vehiculo()}: {vehiculo.describir()}")


# Bloque principal del programa
if __name__ == "__main__":
    print("DEMOSTRACIÓN DE PROGRAMACIÓN ORIENTADA A OBJETOS")
    print("=============================================\n")

    # Creación de instancias
    vehiculo_generico = Vehiculo("Genérica", "Modelo X", 2020)
    mi_auto = Automovil("Toyota", "Corolla", 2022, 4)
    mi_moto = Motocicleta("Honda", "CBR600", 2021, 600)

    # Demostración de herencia y encapsulación
    print("\n--- Herencia y Encapsulación ---")
    print(vehiculo_generico.describir())
    print(mi_auto.describir())
    print(mi_moto.describir())

    mi_auto.avanzar(150)
    print(f"Kilometraje del auto: {mi_auto.get_kilometraje()} km")
    print(f"Número de puertas: {mi_auto.get_num_puertas()}")

    # Demostración de polimorfismo
    print("\n--- Polimorfismo ---")
    mostrar_tipo(vehiculo_generico)
    mostrar_tipo(mi_auto)
    mostrar_tipo(mi_moto)

    # Métodos específicos de cada clase
    print("\n--- Métodos Específicos ---")
    mi_auto.abrir_puertas()
    mi_moto.hacer_caballito()