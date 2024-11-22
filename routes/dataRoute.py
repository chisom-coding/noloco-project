import http3
from fastapi import APIRouter

from models.whereFilter import WhereFilter
from services.dataService import dataService
from services.schemaService import schemaService

router = APIRouter()

client = http3.AsyncClient()

async def call_api(url: str):
    res = await client.get(url)
    return res.json()

@router.post("/data")
async def request_data(filter: WhereFilter):
    data = await call_api("https://app-media.noloco.app/noloco/dublin-bikes.json")
    if not data or len(data) == 0:
        return []

    service1 = dataService()
    service2 = schemaService()
    schema = service2.get_schema(data)
    response = service1.request_data(data, filter.where, schema)

    return response

@router.get("/data/{id}")
async def get_station(id: int):
    data = await call_api("https://app-media.noloco.app/noloco/dublin-bikes.json")
    if not data or len(data) == 0:
        return []

    service = dataService()
    response = service.get_station_by_id(id, data)

    return response

@router.delete("/data/{id}")
async def delete_station(id: int):
    data = await call_api("https://app-media.noloco.app/noloco/dublin-bikes.json")
    if not data or len(data) == 0:
        return []

    service = dataService()
    response = service.delete_station_by_id(id, data)

    if response == 200:
        return {"message" : f"Station {id} was deleted"}


## UPDATE STATION HERE ##