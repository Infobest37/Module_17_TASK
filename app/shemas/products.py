from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    category_id: int # Поле для указания, к какой категории относится продукт.

    class Config:
        orm_mode = True
class ProductCreate(BaseModel): # Используется только для создания или обновления продукта.
    name: str
    category_id: int
