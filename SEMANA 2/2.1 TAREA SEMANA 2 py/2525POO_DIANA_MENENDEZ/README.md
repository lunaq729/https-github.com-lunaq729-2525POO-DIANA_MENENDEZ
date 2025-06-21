# 2525POO_DIANA_MENENDEZ
LUNA
clase Personaje:

    definición __init__(ser,nombre,fuerza,inteligencia,defensa,vida):
        ser.nombre = nombre
        ser.fuerza = fuerza
        ser.inteligencia = inteligencia
        ser.defensa = defensa
        ser.vida = vida

    definición Atributos(ser):
        imprimir(ser.nombre,":",sep="")
        imprimir("·Fuerza:",ser.fuerza)
        imprimir("·Inteligencia:",ser.inteligencia)
        imprimir("·Defensa:",ser.defensa)
        imprimir("·Vida:",ser.vida)

    definición subir_nivel(ser,fuerza,inteligencia,defensa):
        ser.fuerza = ser.fuerza + fuerza
        ser.inteligencia = ser.inteligencia + inteligencia
        ser.defensa = ser.defensa + defensa

    definición esta_vivo(ser):clase Personaje:

    definición __init__(ser,nombre,fuerza,inteligencia,defensa,vida):
        ser.nombre = nombre
        ser.fuerza = fuerza
        ser.inteligencia = inteligencia
        ser.defensa = defensa
        ser.vida = vida

    definición Atributos(ser):
        imprimir(ser.nombre,":",sep="")
        imprimir("·Fuerza:",ser.fuerza)
        imprimir("·Inteligencia:",ser.inteligencia)
        imprimir("·Defensa:",ser.defensa)
        imprimir("·Vida:",ser.vida)

    definición subir_nivel(ser,fuerza,inteligencia,defensa):
        ser.fuerza = ser.fuerza + fuerza
        ser.inteligencia = ser.inteligencia + 
        devolver ser.vida > 0

    definición morir(ser):
        ser.vida = 0
        imprimir(ser.nombre,"ha muerto")

    definición daño(ser,enemigo):
        devolver ser.fuerza - enemigo.defensa

    definición atacar(ser,enemigo):
        daño = ser.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        imprimir(ser.nombre,"ha realizado",daño,"puntos de daño a",enemigo.nombre)
        si enemigo.esta_vivo():
            imprimir("Vida de",enemigo.nombre,"es",enemigo.vida)
        demás:
            enemigo.morir()


clase Guerrero(Personaje):

    definición __init__(ser,nombre,fuerza,inteligencia,defensa,vida,espada):
        súper().__init__(nombre,fuerza,inteligencia,defensa,vida)
        ser.espada = espada

    definición cambiar_arma(ser):
        opción = entero(aporte("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10"))
        si opción == 1:
            ser.espada = 8
        Elif opción == 2:
            ser.espada = 10
        demás:
            imprimir(Número de arma incorrecto)

    definición Atributos(ser):
        súper().Atributos()
        imprimir("·Espada:",ser.espada)

    definición daño(ser,enemigo):
        devolver ser.fuerza * ser.espada - enemigo.defensa


clase Mago(Personaje):

    definición __init__(ser,nombre,fuerza,inteligencia,defensa,vida,libro):
        súper().__init__(nombre,fuerza,inteligencia,defensa,vida)
        ser.libro = libro

    definición Atributos(ser):
        súper().Atributos()
        imprimir("·Libro:",ser.libro)

    definición daño(ser,enemigo):
        devolver ser.inteligencia * ser.libro - enemigo.defensa


definición combate(jugador_1,jugador_2):
    turno = 0
    mientras jugador_1.esta_vivo()y jugador_2.esta_vivo():
        imprimir("\norteTurno",turno)
        imprimir(">>> Acción de ",jugador_1.nombre,":",sep="")
        jugador_1.atacar(jugador_2)
        imprimir(">>> Acción de ",jugador_2.nombre,":",sep="")
        jugador_2.atacar(jugador_1)
        turno = turno + 1
    si jugador_1.esta_vivo():
        imprimir("\norte"Ha ganado",jugador_1.nombre)
    Elif jugador_2.esta_vivo():
        imprimir("\norte"Ha ganado",jugador_2.nombre)
    demás:
        imprimir("\norteEmpate")


personaje_1 = Guerrero("Vísceras",20,10,4,100,4)
personaje_2 = Mago("Vanessa",5,15,4,100,3)

personaje_1.Atributos()
personaje_2.Atributos()

combate(personaje_1,personaje_2)