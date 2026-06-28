class restaurant:

    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Direccion: {self.direccion}, Telefono: {self.telefono}"

    def __str__(self):
        return f"Nombre: {self.nombre}, Direccion: {self.direccion}, Telefono: {self.telefono}"
