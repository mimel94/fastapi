from re import S
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id : Optional[str]
    name : str
    email: str
    password: str

class Empleado(BaseModel):
    id: Optional[str]
    cc: str
    nombre:str
    apellido:str
    telefono:str
    email:str
    fecha_contratacion:str

class Proyecto(BaseModel):
    id:Optional[str]
    nombre: str
    denominacion: str
    fecha_inicio: str
    fecha_finalizacion: str
    estado_actual: str
    ciudad: str
    id_empleado: str

class Tareas(BaseModel):
    id:Optional[str]
    descripcion: str
    tipo: str
    fecha_inicio_estimada: str
    fecha_inicio: str
    duracion_estimada: str
    duracion_real: str
    id_proyecto: str

class DocumentoGenerado(BaseModel):
    id:Optional[str]
    descripcion: str
    tipo: str
    id_tarea: str

class VersionDocumento(BaseModel):
    id:Optional[str]
    descripcion: str
    fecha: str
    id_documento: str