    passclass Evento:
    def_init_self, id: int, nombre: str,
     artista: str, genero: str, 
     id_ubicacion: int, 
     hora_inicio: str, hora_fin: str. 
     descripcion: str, 
         """
         hora_inicio datetime ISO 8601
         hora_fin datetime ISO 8601
         imagen URL apuntar a un archivo en la carpeta assets
         """


     imagen: str ):
         self.id = id
         self.nombre = nombre 
         self.artista = artista
         self.genero = genero
         self.id_ubicacion = id_ubicacion
         self.hora_inicio = hora_inicio
         self.hora_fin = hora_fin
         self.imagen = imagen
evento = Evento()         

def to_json(self):
    pass
@classmethod
def from_json(self):
