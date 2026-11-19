class Cliente:
    def __init__(self,nombre,dni,telefono,email):
        self.nombre=nombre
        self.dni=dni
        self.telefono=telefono
        self.email=email
    def mostrar_informacion(self):
        print(f"----Informacion del Cliente----")
        print(f"Nombre: {self.nombre} ")
        print(f"DNI: {self.dni}")
        print(f"Telefono: {self.telefono}")
        print(f"Email: {self.telefono}")
    
    def validar(self):
        if self.nombre.strip() == "" or self.dni <= 0 or self.email.strip()=="" or self.telefono.strip()=="":
            return False

        return True
    
    

        