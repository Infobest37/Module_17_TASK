from fastapi import APIRouter, HTTPException
from app.shemas.category import Category, CategoryCreate

router = APIRouter(prefix="/categories", tags=["Categories"],)
categories = [
    {"id": 1, "name": "Elecnronics", "description": "Elecnronics TV"},
    {"id": 2, "name": "Fords", "description": "Fords TV"},
    {"id": 3, "name": "Honda", "description": "Honda TV"}
]
@router.get("/", response_model=list[Category])
async def get_all_categories():
    return categories

@router.post("/create", response_model=Category)
async def create_category(category: Category):
    """Создает новую категорию"""
    new_category = {"id": len(categories)+1, "name": category.name, "description": category.description}
    categories.append(new_category)
    return new_category
@router.put("/update_category", response_model=Category)
async def update_category(category_id: int, category: CategoryCreate):
    """Обновить категорию"""
    for cat in categories:
        if cat["id"] == category_id:
            cat["name"] = category.name
            cat["description"] = category.description
            return cat
    raise HTTPException(status_code=404, detail="Category not found")
@router.delete("/delete_category")
async def delete_category(category_id: int):
    """Удалить категорию"""
    global categories
    categories = [cat for cat in categories if cat["id"] != category_id]
    return "Категория удалена"