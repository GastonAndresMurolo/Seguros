

class Sistema_seguros:
    def __init__(self):
        self.clientes=[]
        
    def agregar_cliente(self,cliente):
        if cliente.validar():
            self.clientes.append(cliente)
            return True
        
        return False
    
    def mostrar_clientes(self):
        if len(self.clientes) == 0:
            print("No hay clientes registrados")
            return
        for cliente in self.clientes:
            cliente.mostrar_informacion()
            print("-------------------")
    