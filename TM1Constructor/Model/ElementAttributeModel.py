from pydantic import BaseModel
from TM1py.Objects import ElementAttribute

class ElementAttributeModel(BaseModel):
    Name: str
    Type: ElementAttribute.Types