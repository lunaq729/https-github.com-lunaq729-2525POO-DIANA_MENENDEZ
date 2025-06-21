# Definición de constantes
DIAS_SEMANA = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
NUM_DIAS = 7

def obtener_temperatura(dia): Lunes;
    """
    Solicita al usuario la temperatura para un día específico con validación
    """
    while True:
        try:
            temp = float(input(f"Ingrese la temperatura para el {dia} (°C): "))
            return temp
        except ValueError:
            print("Error: Por favor ingrese un valor numérico válido.")

def registrar_temperaturas():
    """
    Registra las temperaturas para los 7 días de la semana
    """
    temperaturas = []
    print("\nREGISTRO DE TEMPERATURAS SEMANALES")
    
    for dia in DIAS_SEMANA:
        temperatura = obtener_temperatura(dia)
        temperaturas.append(temperatura)
    
    return temperaturas
