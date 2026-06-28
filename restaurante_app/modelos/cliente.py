class cliente:
    def __init__(self, nombre, apellido, telefono, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo

    def mostrar_informacion(self):    
        return f"nombre: {self.nombre}, apellido: {self.apellido}, telefono: {self.telefono}, correo: {self.correo}"
    
    def __str__(self):
        return f"nombre: {self.nombre}, apellido: {self.apellido}, telefono: {self.telefono}, correo: {self.correo}"
