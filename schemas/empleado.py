def empleadoEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "cc":item["cc"],
        "nombre":item["nombre"],
        "apellido":item["apellido"],
        "telefono":item["telefono"],
        "email":item["email"],
        "fecha_contratacion":item["fecha_contratacion"]
    }

def empleadosEntity(entity) -> list:
    return [empleadoEntity(item) for item in entity]