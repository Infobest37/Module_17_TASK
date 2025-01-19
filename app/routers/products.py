

from fastapi import APIRouter, HTTPException
from app.shemas.products import Product, ProductCreate


router = APIRouter(prefix="/products", tags=["Products"]) # Группа маршрутов для документации

products = [
    {"id": 1, "name": "Apel", "category_id": 1},
    {"id": 2, "name": "Mebel", "category_id": 2},
    {"id": 3, "name": "Pizza", "category_id": 3},
]
@router.get("/")
async def get_all_products():
    return products


@router.post("/create", response_model=Product) # Для добавления новых продуктов
async def create_product(product: ProductCreate):
    new_product = {"id": len(products)+1, "name": product.name, "category_id": product.category_id}
    products.append(new_product)
    return new_product

@router.put("/update_product")
async def update_product(product_id: int, product: Product):
    for prod in products:
        if prod["id"] == product_id:
            prod["name"] = product.name
            prod["category_id"] = product.category_id
            return prod
    raise HTTPException(status_code=404, detail="Product not found")

@router.delete("/delete_product")
async def delete_product(product_id: int):
    global products
    products = [prod for prod in products if prod["id"] != product_id]
    return "Продукт удален"
