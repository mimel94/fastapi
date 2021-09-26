def documentoEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "descripcion":item["descripcion"],
        "tipo":item["tipo"],
        "id_tarea":item["id_tarea"]
    }

def documentosEntity(entity) -> list:
    return [documentoEntity(item) for item in entity]