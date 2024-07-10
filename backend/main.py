from fastapi import FastAPI
from routers.currency import router as router_currency

app = FastAPI()

app.include_router(router_currency)


@app.get("/")
async def root():
    return {"message": "Currency app"}
