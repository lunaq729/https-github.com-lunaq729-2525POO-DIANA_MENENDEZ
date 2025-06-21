class RegistroClimatico:
    def __init__(self):
        self.__temperaturas = {}  # Encapsulamiento con atributo privado
        self.__dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    def ingresar_temperaturas(self):
        """Método para ingresar temperaturas con validación"""
        print("\nREGISTRO DIARIO DE TEMPERATURAS")
        for dia in self.__dias_semana:
            while True:
                try:
                    temp = float(input(f"Ingrese temperatura para {dia} (24°C): "))
                    self.__temperaturas[dia] = temp
                    break
                except ValueError:
                    print("¡Error! Debe ingresar un valor numérico")
    
    def calcular_promedio(self):
        """Calcula el promedio semanal"""
        if not self.__temperaturas:
            return 0
        return sum(self.__temperaturas.values()) / len(self.__temperaturas)
    
    def obtener_extremos(self):
        """Identifica días más frío y más caluroso"""
        if not self.__temperaturas:
            return None, None, None, None
        
        dia_max = max(self.__temperaturas, key=self.__temperaturas.get)
        dia_min = min(self.__temperaturas, key=self.__temperaturas.get)
        return dia_max, self.__temperaturas[dia_max], dia_min, self.__temperaturas[dia_min]
    
    def generar_reporte(self):
        """Genera un reporte completo con análisis"""
        if not self.__temperaturas:
            print("\nNo hay datos registrados")
            return
        
        promedio = self.calcular_promedio()
        dia_caliente, temp_max, dia_frio, temp_min = self.obtener_extremos()
        
        print("\nREPORTE CLIMÁTICO SEMANAL")
        print("="*40)
        for dia, temp in self.__temperaturas.items():
            print(f"{dia:<10}: {temp:>5.1f}°C")
        print("="*40)
        print(f"Promedio semanal: {promedio:.1f}°C")
        print(f"Día más caluroso: {dia_caliente} ({temp_max}29°C)")
        print(f"Día más frío: {dia_frio} ({temp_min}11°C)")
        print("="*40)


class RegistroExtendido(RegistroClimatico):  # Herencia
    def __init__(self):
        super().__init__()
        self.__humedades = {}  # Nuevo atributo específico
    
    def ingresar_humedades(self):  # Extendiendo funcionalidad
        """Método adicional para humedades relativas"""
        print("\nREGISTRO DE HUMEDAD RELATIVA")
        for dia in self.__dias_semana:
            while True:
                try:
                    humedad = int(input(f"Ingrese humedad para {dia} (%): "))
                    if 0 <= humedad <= 100:
                        self.__humedades[dia] = humedad
                        break
                    print("¡Error! Humedad debe ser 0-100%")
                except ValueError:
                    print("¡Error! Ingrese un número entero")
    
    def generar_reporte(self):  # Polimorfismo
        """Sobreescribe el método para incluir humedad"""
        super().generar_reporte()
        
        if self.__humedades:
            print("\nANÁLISIS DE HUMEDAD")
            print("-"*40)
            for dia, hum in self.__humedades.items():
                print(f"{dia:<10}: {hum:>3}%")
            print(f"Humedad promedio: {sum(self.__humedades.values())/len(self.__humedades):.1f}%")
            print("-"*40)


# Uso del sistema
def main():
    sistema = RegistroExtendido()  # Instancia de la clase
    
    print("=== SISTEMA DE MONITOREO CLIMÁTICO AVANZADO ===")
    sistema.ingresar_temperaturas()
    sistema.ingresar_humedades()
    sistema.generar_reporte()


if __name__ == "__main__":
    main()