import http3
from fastapi import APIRouter
from services.schemaService import schemaService

router = APIRouter()

client = http3.AsyncClient()

# fetching the data from the url given
async def call_api(url: str):
    res = await client.get(url)
    return res.json()

@router.get("/schema")
async def get_schema():
    data = await call_api("https://app-media.noloco.app/noloco/dublin-bikes.json")
    if not data or len(data) == 0:
        return []

    service = schemaService()
    response = service.get_schema(data)

    return response