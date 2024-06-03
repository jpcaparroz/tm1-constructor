from pydantic import BaseModel
from typing import Dict

class CaptionModel(BaseModel):
    translations: Dict[str, str]
    