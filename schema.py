from datetime import datetime
from pydantic import BaseModel, Field as PydanticField
from typing import Optional
from bson import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")



class AlunoCriacaoSchema(BaseModel):
    nome: Optional[str] = None
    idade: Optional[int] = None
    curso: Optional[str] = None

    
class AlunoSchema(BaseModel):
    id: PyObjectId = PydanticField(default_factory=PyObjectId, alias="_id")
    nome: str
    idade: int
    curso: str
    data_criacao: datetime
    
    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
