from models.notion import Certificate

def certificateEntity(item) -> dict:

    certificate = {
        "name": item.get("properties", {}).get("Nombres y Apellidos", "").get("title", {})[0].get("plain_text", ""),
        "document": item.get("properties", {}).get("DNI", "").get("rich_text", {})[0].get("plain_text", ""),
        "course": {
            "code": item.get("properties", {}).get("Code Course", "").get("rollup", {}).get("array", {})[0].get("rich_text", {})[0].get("plain_text", ""),
            "name": item.get("properties", {}).get("Course", "").get("formula", {}).get("string", ""),
            "date_start": item.get("properties", {}).get("Date Course", "").get("formula", {}).get("string", ""),
            "hours": item.get("properties", {}).get("Hours Course", "").get("formula", {}).get("string", "")
        },
        "date": item.get("properties", {}).get("Fecha de Emisión", "").get("date", {}).get("start", ""),
        "hash": item.get("properties", {}).get("Hash", "").get("formula", {}).get("string", ""),
        "url": item.get("properties", {}).get("Link de Certificado", "").get("formula", {}).get("string", "")
    }

    #Converti BaseModel a Dict
    certificate_base_model = Certificate(**certificate)
    certificate_dict = certificate_base_model.model_dump(by_alias=True, exclude_unset=True)
    return certificate_dict

def certificateEntitys(entity):
    return [certificateEntity(item) for item in entity]
