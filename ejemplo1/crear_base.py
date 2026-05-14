from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

from configuracion import engine


from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Saludo(Base):
    __tablename__ = 'saludos'
    id = Column(Integer, primary_key=True)
    mensaje = Column(String(200))
    tipo = Column(String(200))

    def __str__(self): #self es el nombre de la instancia del objeto, es decir, el objeto que se esta creando a partir de la clase Saludo.
        return f"{self.id} - {self.mensaje} - {self.tipo}"


class Saludo2(Base):
    __tablename__ = 'saludo_dos'
    id = Column(Integer, primary_key=True)
    mensaje = Column(String(200))
    tipo = Column(String(200))
    origen = Column(String(200))

    def __str__(self):
        return f"{self.id} - {self.mensaje} - {self.tipo} - {self.origen}"

Base.metadata.create_all(engine)
