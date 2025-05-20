from datetime import date, time
import uuid # Necesario para id_reserva

# Asumimos que las clases Usuario y Sala están definidas en otros módulos o se pasarán como BIND_TYPES
# Por simplicidad del ejemplo, no las importamos explícitamente aquí si este es un módulo aislado.
# class Usuario: pass
# class Sala: pass

class Reserva:
    def __init__(self, fecha: date, hora_inicio: time, hora_fin: time, usuario: 'Usuario', sala: 'Sala'):
        self.__id_reserva = str(uuid.uuid4()) # NUEVO: Identificador único de reserva
        self.__fecha = fecha
        self.__hora_inicio = hora_inicio # Corregido: Debería ser hora_inicio
        self.__hora_fin = hora_fin
        self.__usuario = usuario 
        self.__sala = sala     

    @property
    def id_reserva(self): # NUEVO
        return self.__id_reserva

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
        # Deberías tener una forma de acceder al nombre del usuario si es necesario para __str__
        # por ejemplo, self.__usuario.nombre
        return self.__usuario

    @property
    def sala(self):
        # Deberías tener una forma de acceder al nombre de la sala si es necesario para __str__
        # por ejemplo, self.__sala.nombre
        return self.__sala

    def modificarReserva(self, nueva_fecha: date, nueva_hora_inicio: time, nueva_hora_fin: time): # Nombre de método como en el UML
        # Lógica de validación aquí si es necesaria
        self.__fecha = nueva_fecha
        self.__hora_inicio = nueva_hora_inicio
        self.__hora_fin = nueva_hora_fin
        print(f"Reserva {self.id_reserva} modificada a fecha {self.fecha}, de {self.hora_inicio} a {self.hora_fin}")

    def __str__(self):
        # Para que esto funcione bien, Usuario y Sala deberían tener un atributo 'nombre' accesible
        # o adaptar el __str__
        user_name = self.__usuario.nombre if hasattr(self.__usuario, 'nombre') else "UsuarioDesconocido"
        sala_name = self.__sala.nombre if hasattr(self.__sala, 'nombre') else "SalaDesconocida"
        return f"Reserva ID: {self.id_reserva}, Sala: '{sala_name}', Usuario: '{user_name}', Fecha: {self.fecha}, De: {self.hora_inicio} a {self.hora_fin}"

# Ejemplo de uso (requeriría stubs o definiciones completas de Usuario y Sala)
# if __name__ == '__main__':
#     # Mock/Stub para Usuario y Sala para que el ejemplo funcione
#     class MockUsuario:
#         def __init__(self, nombre): self.nombre = nombre
#     class MockSala:
#         def __init__(self, nombre): self.nombre = nombre

#     user1 = MockUsuario("Test User")
#     sala1 = MockSala("Test Sala")
    
#     res = Reserva(date(2025,12,24), time(10,0), time(12,0), user1, sala1)
#     print(res)
#     res.modificarReserva(date(2025,12,25), time(14,0), time(16,0))
#     print(res)
