from pydantic import BaseModel


class ViewModel(BaseModel):
    Name: str
    MDX: str
    Default: bool