from fastapi import FastAPI
from routers import category, products

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Мой магазин"}

app.include_router(category.router)
app.include_router(products.router)
