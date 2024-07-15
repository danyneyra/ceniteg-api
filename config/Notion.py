import os
from dotenv import load_dotenv
from notion_client import APIErrorCode, APIResponseError, Client
from schemas.notion import certificateEntitys

load_dotenv()

def certificateQuery(property, value):

    notion_key=os.getenv('NotionKey')
    notion_db=os.getenv('NotionDB_Certificados')

    # set up the Notion client
    notion = Client(auth=notion_key)

    # get the database
    database_id = notion_db

    # create a filter notion
    filter_search = str(property).lower()

    if filter_search == "dni":
        filter_params = {
            "property": "DNI",
            "rich_text": {
                "equals": str(value)
            }
        }
    elif filter_search == "hash":
        filter_params = {
            "property": "Hash",
            "formula": {
                "string":{
                    "contains": str(value)
                }
            }
        }
    else:
        print("ERROR: EL filtro es incorrecto")
        return {"result": "error", "message": "filter is incorrect"}

    try:
        # query the database with the filter notion
        results = notion.databases.query(
            **{
                "database_id": database_id,
                "filter": filter_params
            }
        )

        if not results.get("results"):
            return {"result": "error", "message": "Nothing was found"}
        else:
            results = certificateEntitys(results.get("results"))

    except APIResponseError as error:
        if error.code == APIErrorCode.ObjectNotFound:
            ...  # For example: handle by asking the user to select a different database
            print('NOTION: Error en la API de Notion')
            message = str(error)
        else:
            # Other error handling code
            print('NOTION: ' + str(error))
            message = str(error)
        
        return {"result": "error", "message": message}


    # print the results
    return results