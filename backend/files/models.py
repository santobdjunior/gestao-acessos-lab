from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship

from .database import Base

from enum import Enum as EnumDB

class DepartamentoEnum(str, EnumDB):
    ADMINISTRATIVO = "Admnistrativo"
    COMERCIAL = "Comercial"
    TECNOLOGIA = "Tecnologia"
    MARKETING = "Marketing"

class Usuarios(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    nome = Column(String, index=True)
    departamento = Column(Enum(DepartamentoEnum),index=True)
    telefone = Column(String, index=True)
# hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


