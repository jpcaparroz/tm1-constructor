from pydantic import BaseModel
from TM1py.Objects import Element

class ElementModel(BaseModel):
    Name: str
    Type: Element.Types