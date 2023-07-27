class RutaVisita:
    def_init_(self, id: int, nombre: str,
    destino: list[int]):
        self.id = id
        self.nombre = nombre
        self.destino = destino

    def to_json(self):
        pass

    @classmethod
    def from_json(self):
        pass  