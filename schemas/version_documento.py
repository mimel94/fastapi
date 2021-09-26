def versionDocumentoEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "descripcion":item["descripcion"],
        "fecha":item["fecha"],
        "id_documento":item["id_documento"]
    }

def versionDocumentosEntity(entity) -> list:
    return [versionDocumentoEntity(item) for item in entity]