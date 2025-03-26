from pydantic import BaseModel
from typing import Optional

class CurrentLocationSchema(BaseModel):
    ip : str
    lon : float
    lat : float
    country : str

class LocationSchema(BaseModel):
    country : str
    city : Optional[str]
    formatted:str
    lat : float
    lon : float
    state : Optional[str]