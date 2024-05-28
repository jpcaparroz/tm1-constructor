from pydantic import BaseModel
from typing import Optional

class SubsetModel(BaseModel):
    Name: str
    MDX: str
    Elements: Optional[list[str]]
    Alias: Optional[str] = None
    Default: bool = False