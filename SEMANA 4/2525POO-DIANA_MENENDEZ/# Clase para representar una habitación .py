# Clase para representar una habitación de hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo  # Ejemplo: 'simple', 'doble', 'suite'
        self.precio = precio
        self.disponible = True

    def ocupar(self):
        self.disponible = False

    def liberar(self):
        self.disponible = True

# Clase para representar un cliente
class Cliente:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.reservas = []

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)

# Clase para representar una reserva
class Reserva:
    def __init__(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias

    def calcular_total(self):
        return self.dias * self.habitacion.precio

# Clase principal para gestionar el hotel
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []
        self.reservas = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def buscar_habitacion_disponible(self, tipo):
        for hab in self.habitaciones:
            if hab.tipo == tipo and hab.disponible:
                return hab
        return None

    def reservar(self, cliente, tipo, dias):
        habitacion = self.buscar_habitacion_disponible(tipo)
        if habitacion:
            habitacion.ocupar()
            reserva = Reserva(cliente, habitacion, dias)
            self.reservas.append(reserva)
            cliente.agregar_reserva(reserva)
            print(f"Reserva confirmada para {cliente.nombre} en habitación {habitacion.numero}")
        else:
            print("No hay habitaciones disponibles de ese tipo.")

# Ejemplo de uso
hotel = Hotel("Hotel Central")
hotel.agregar_habitacion(Habitacion(101, "simple", 100))
hotel.agregar_habitacion(Habitacion(102, "doble", 180))

cliente1 = Cliente("Ana Pérez", "12345678")
hotel.reservar(cliente1, "simple", 3)
