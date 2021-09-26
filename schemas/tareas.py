def tareaEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "descripcion":item["descripcion"],
        "tipo":item["tipo"],
        "fecha_inicio_estimada":item["fecha_inicio_estimada"],
        "fecha_inicio":item["fecha_inicio"],
        "duracion_estimada":item["duracion_estimada"],
        "duracion_real":item["duracion_real"],
        "id_proyecto":item["id_proyecto"]
    }

def tareasEntity(entity) -> list:
    return [tareaEntity(item) for item in entity]