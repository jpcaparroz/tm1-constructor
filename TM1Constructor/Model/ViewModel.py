from pydantic import BaseModel

from typing import Optional


class ViewModel(BaseModel):
    Name: str
    MDX: Optional[str]
    Default: bool