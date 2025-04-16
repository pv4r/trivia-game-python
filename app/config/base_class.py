from typing import Any
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative


@as_declarative()
class Base: # Clase base para los modelos de SQLAlchemy
    id: Any
    __name__: str

    # Este metodo se utiliza para definir el nombre de la tabla
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
