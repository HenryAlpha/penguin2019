#  crear clase persona con atributo nombre

class Persona:

    nombre = None

    def __init__(self, el_nombre):
        self.nombre = el_nombre
        print("Soy una persona y mi nombre es:", self.nombre)

    def set_nombre(self, nombre):
        self.nombre = nombre

Freddie= Persona("Freddie")
