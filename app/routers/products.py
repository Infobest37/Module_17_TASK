from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["product"])
@router.get("/all_products")
async def get_all_products():
    pass

@router.post("/create")
async def create_product(name: str):
    pass
@router.put("/update_product")
async def update_product(name: str):
    pass

@router.delete("/delete_product")
async def delete_product(name: str):
    pass

