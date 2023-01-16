class Cliente:
    nombre = ""
    matricula = ""

    def __init__(self,nombre,matricula):
        self.nombre = nombre
        self.matricula = matricula

    def __str__(self):
        return f"NOMBRE\t\t {self.nombre}\n" \
               f"MATRÍCULA\t {self.matricula}\n"



class Abonado(Cliente):
    plaza = 0

    def __str__(self):
        return f"NOMBRE\t\t {self.nombre}\n" \
               f"MATRÍCULA\t {self.matricula}\n" \
               f"PLAZA\t {self.plaza}\n"




