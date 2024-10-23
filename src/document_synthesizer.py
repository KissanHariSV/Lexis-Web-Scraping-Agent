from pydantic import BaseModel
from typing import List

class Document(BaseModel):
    url: str
    summary: str
    headers: List[str] 
