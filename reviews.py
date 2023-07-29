class Reviews:
    def_init_self, id: int, id_evento: int,
    id_usuario: int, calificacion: int,
    comentario: str, animo: str):
        """
        calificacion int del 1 al 5
        animo str "positivo" / "negativo"
        """     
        self.id = id
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

    def to_json(self):
        pass

    @classmethod
    def from_json(self):
        pass        
