class Ubicacion:
    def_init_self, id: int, nombre: str,
    direccion: str, coordenadas: list[float]):
         self.id = id
         self.nombre = nombre
         self.direccion = direccion
         self.cordenadas = coordenadas

    def to_json(self):
        pass

    @classmethod
    def from_json(self):
        pass         