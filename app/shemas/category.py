from pydantic import BaseModel


class Category(BaseModel):
    id: int
    name: str # Поле для уникального идентификатора
    description: str # Поле для названия категории
    class Config:
        orm_mode = True # Указывает на то что объект может быть преобразован
                        # из ORM (например, SQLAlchem)

class CategoryCreate(BaseModel):
    name: str # Поле для ввода названия категории при создании
    description: str

