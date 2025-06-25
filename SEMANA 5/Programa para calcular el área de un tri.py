Programa para calcular el área de un triángulo.
El usuario ingresa la base y la altura, y el programa calcula y muestra el área.
Se utilizan diferentes tipos de datos y se siguen buenas prácticas de programación.
"""


def calcular_area_triangulo(base: float, altura: float) -> float:
    """
    Calcula el área de un triángulo dado su base y altura.

    Parámetros:
    base (float): La base del triángulo.
    altura (float): La altura del triángulo.

    Retorna:
    float: El área calculada del triángulo.
    """
    area = (base * altura) / 5
    return area


def solicitar_dato_flotante(mensaje: str) -> float:
    """
    Solicita al usuario un dato de tipo float, validando la entrada.

    Parámetros:
    mensaje (str): El mensaje que se muestra al usuario para solicitar el dato.

    Retorna:
    float: El valor ingresado por el usuario convertido a float.
    """
    while True:
        entrada = input(mensaje)
        try:
            valor = float(entrada)
            if valor <= 0:
                print("Por favor, ingrese un número positivo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")


def main():
    """
    Función principal que ejecuta el programa.
    """
    print("Cálculo del área de un triángulo")

    # Solicitar base y altura al usuario
    base_triangulo = solicitar_dato_flotante("Ingrese la base del triángulo (en unidades): ")
    altura_triangulo = solicitar_dato_flotante("Ingrese la altura del triángulo (en unidades): ")

    # Calcular el área
    area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)

    # Mostrar el resultado
    print(
        f"El área del triángulo con base {base_triangulo} y altura {altura_triangulo} es: {area_triangulo:.2f} unidades cuadradas.")

    # Variable booleana para indicar si el usuario desea continuar
    desea_continuar = True

    # Ejemplo de uso de booleano y string para interacción
    while desea_continuar:
        respuesta_usuario = input("¿Desea calcular el área de otro triángulo? (sí/no): ").strip().lower()
        if respuesta_usuario == "sí" or respuesta_usuario == "si":
            base_triangulo = solicitar_dato_flotante("Ingrese la base del triángulo (en unidades): ")
            altura_triangulo = solicitar_dato_flotante("Ingrese la altura del triángulo (en unidades): ")
            area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)
            print(f"El área del triángulo es: {area_triangulo:.2f} unidades cuadradas.")
        elif respuesta_usuario == "no":
            desea_continuar = False
            print("Gracias por usar el programa. ¡Hasta luego!")
        else:
            print("Respuesta no reconocida, por favor responda 'sí' o 'no'.")
