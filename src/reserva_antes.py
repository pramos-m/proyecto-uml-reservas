from datetime import date, time

# Asumimos que las clases Usuario y Sala están definidas en otros módulos o se pasarán como tipos.
# class Usuario: pass 
# class Sala: pass

class Reserva:
    def __init__(self, fecha: date, hora_inicio: time, hora_fin: time, usuario: 'Usuario', sala: 'Sala'):
        self.__fecha = fecha
        self.__hora_inicio = hora_inicio
        self.__hora_fin = hora_fin
        self.__usuario = usuario 
        self.__sala = sala     

    @property
    def fecha(self):
        return self.__fecha

    @property
    def hora_inicio(self):
        return self.__hora_inicio

    @property
    def hora_fin(self):
        return self.__hora_fin
    
    @property
    def usuario(self):
        return self.__usuario

    @property
    def sala(self):
        return self.__sala

    def modificarReserva(self, nueva_fecha: date, nueva_hora_inicio: time, nueva_hora_fin: time):
        self.__fecha = nueva_fecha
        self.__hora_inicio = nueva_hora_inicio
        self.__hora_fin = nueva_hora_fin
        print(f"Reserva modificada a fecha {self.fecha}, de {self.hora_inicio} a {self.hora_fin}")

    def __str__(self):
        user_name = self.__usuario.nombre if hasattr(self.__usuario, 'nombre') else "UsuarioDesconocido"
        sala_name = self.__sala.nombre if hasattr(self.__sala, 'nombre') else "SalaDesconocida"
        return f"Reserva: Sala '{sala_name}', Usuario: '{user_name}', Fecha: {self.fecha}, De: {self.hora_inicio} a {self.hora_fin}"
