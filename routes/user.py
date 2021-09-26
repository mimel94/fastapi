from typing import List
from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.user import userEntity, usersEntity
from schemas.empleado import empleadoEntity, empleadosEntity
from schemas.proyectos import proyectoEntity, proyectosEntity
from schemas.tareas import tareaEntity, tareasEntity
from schemas.version_documento import versionDocumentoEntity, versionDocumentosEntity
from schemas.documento_generado import documentoEntity, documentosEntity
from models.user import Empleado, User, Proyecto,Tareas, DocumentoGenerado, VersionDocumento
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
from typing import List
user = APIRouter()

#----Empleados----

@user.get('/empleados', response_model=List[Empleado])
def find_all_empleados():
    return empleadosEntity(conn.local.empleado.find())


@user.post('/empleado', response_model=Empleado)
def create_empleado(empleado: Empleado):
    nuevo_empleado = dict(empleado)    
    del nuevo_empleado["id"]
    id = conn.local.empleado.insert_one(nuevo_empleado).inserted_id
    empleado = conn.local.empleado.find_one({"_id": id})
    return empleadoEntity(empleado)


@user.get('/empleado/{id}', response_model=Empleado)
def find_empleado(id: str):
    return empleadoEntity(conn.local.empleado.find_one({"_id": ObjectId(id)}))


@user.put('/empleado/{id}', response_model=Empleado)
def update_empleado(id: str, empleado: Empleado):
    conn.local.empleado.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(empleado)})
    return empleadoEntity(conn.local.empleado.find_one({"_id": ObjectId(id)}))


@user.delete('/empleado/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_empleado(id: str):
    empleadoEntity(conn.local.empleado.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT
                    )

#Proyecto


@user.get('/proyectos', response_model=List[Proyecto])
def find_all_proyecto():
    return proyectosEntity(conn.local.proyecto.find())


@user.post('/proyecto', response_model=Proyecto)
def create_proyecto(proyecto: Proyecto):
    nuevo_proyecto = dict(proyecto)    
    del nuevo_proyecto["id"]
    id = conn.local.proyecto.insert_one(nuevo_proyecto).inserted_id
    proyecto = conn.local.proyecto.find_one({"_id": id})
    return proyectoEntity(proyecto)


@user.get('/proyecto/{id}', response_model=Proyecto)
def find_proyecto(id: str):
    return proyectoEntity(conn.local.empleado.find_one({"_id": ObjectId(id)}))


@user.put('/proyecto/{id}', response_model=Empleado)
def update_proyecto(id: str, empleado: Empleado):
    conn.local.empleado.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(empleado)})
    return proyectoEntity(conn.local.empleado.find_one({"_id": ObjectId(id)}))


@user.delete('/proyecto/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_proyecto(id: str):
    proyectoEntity(conn.local.empleado.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT
                    )

#---tareas---


@user.get('/tareas', response_model=List[Tareas])
def find_all_tarea():
    return tareasEntity(conn.local.tarea.find())


@user.post('/tarea', response_model=Tareas)
def create_tarea(tarea: Tareas):
    nuevo_tarea = dict(tarea)    
    del nuevo_tarea["id"]
    id = conn.local.tarea.insert_one(nuevo_tarea).inserted_id
    tarea = conn.local.tarea.find_one({"_id": id})
    return tareaEntity(tarea)


@user.get('/tarea/{id}', response_model=Tareas)
def find_tarea(id: str):
    return tareaEntity(conn.local.tarea.find_one({"_id": ObjectId(id)}))


@user.put('/tarea/{id}', response_model=Tareas)
def update_tarea(id: str, tarea: Tareas):
    conn.local.tarea.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(tarea)})
    return tareaEntity(conn.local.tarea.find_one({"_id": ObjectId(id)}))


@user.delete('/tarea/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_tarea(id: str):
    tareaEntity(conn.local.tarea.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT
                    )

#----Documento generado----


@user.get('/documentosGenerados', response_model=List[DocumentoGenerado])
def find_all_documentos_generados():
    return documentosEntity(conn.local.documentos_generados.find())


@user.post('/documentosGenerado', response_model=DocumentoGenerado)
def create_documento(documento_generado: DocumentoGenerado):
    nuevo_documento = dict(documento_generado)    
    del nuevo_documento["id"]
    id = conn.local.documentos_generados.insert_one(nuevo_documento).inserted_id
    documento = conn.local.documentos_generados.find_one({"_id": id})
    return documentoEntity(documento)


@user.get('/documentosGenerado/{id}', response_model=DocumentoGenerado)
def find_documento(id: str):
    return documentoEntity(conn.local.documentos_generados.find_one({"_id": ObjectId(id)}))


@user.put('/documentosGenerado/{id}', response_model=DocumentoGenerado)
def update_documento_generado(id: str, documento: DocumentoGenerado):
    conn.local.documentos_generados.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(documento)})
    return documentoEntity(conn.local.documentos_generados.find_one({"_id": ObjectId(id)}))


@user.delete('/documentosGenerado/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_documento_generado(id: str):
    documentoEntity(conn.local.documentos_generados.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT
                    )



# version del documento----


@user.get('/versionDocumento', response_model=List[VersionDocumento])
def find_all_version_documento():
    return versionDocumentosEntity(conn.local.version_documento.find())


@user.post('/versionDocumento', response_model=VersionDocumento)
def create_documento(documento_generado: VersionDocumento):
    nuevo_documento = dict(documento_generado)    
    del nuevo_documento["id"]
    id = conn.local.version_documento.insert_one(nuevo_documento).inserted_id
    documento = conn.local.version_documento.find_one({"_id": id})
    return versionDocumentoEntity(documento)


@user.get('/versionDocumento/{id}', response_model=VersionDocumento)
def find_documento(id: str):
    return versionDocumentoEntity(conn.local.version_documento.find_one({"_id": ObjectId(id)}))


@user.put('/versionDocumento/{id}', response_model=VersionDocumento)
def update_documento_generado(id: str, documento: VersionDocumento):
    conn.local.version_documento.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(documento)})
    return versionDocumentoEntity(conn.local.version_documento.find_one({"_id": ObjectId(id)}))


@user.delete('/versionDocumento/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_documento_generado(id: str):
    versionDocumentoEntity(conn.local.version_documento.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT
                    )