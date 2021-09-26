def proyectoEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "nombre":item["nombre"],
        "denominacion":item["denominacion"],
        "fecha_inicio":item["fecha_inicio"],
        "fecha_finalizacion":item["fecha_finalizacion"],
        "estado_actual":item["estado_actual"],
        "ciudad":item["ciudad"],
        "id_empleado":item["id_empleado"]
    }

def proyectosEntity(entity) -> list:
    return [proyectoEntity(item) for item in entity]

