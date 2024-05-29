from pydantic import BaseModel

class EdgeModel(BaseModel):
    ParentName: str
    ComponentName: str
    Weight: int