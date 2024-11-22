import uvicorn
from fastapi import FastAPI

from routes import schemaRoute, dataRoute

app = FastAPI()

# retrieving the endpoints from the different routes
app.include_router(schemaRoute.router)
app.include_router(dataRoute.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)