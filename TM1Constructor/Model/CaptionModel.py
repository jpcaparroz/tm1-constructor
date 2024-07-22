from pydantic import BaseModel
from pydantic import ConfigDict


class CaptionModel(BaseModel):
    
    model_config = ConfigDict(extra='allow')
    
    pt: str
    en: str
    