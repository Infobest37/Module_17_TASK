from fastapi import APIRouter

router = APIRouter(prefix="/category", tags=["category"])
@router.get("/all_categories")
async def get_all_categories():
    pass

@router.post("/create")
async def create_category(name: str):
    pass
@router.put("/update_category")
async def update_category(name: str):
    pass

@router.delete("/delete_category")
async def delete_category(name: str):
    pass

