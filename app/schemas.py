from pydantic import BaseModel

class Coordenadas(BaseModel):
    latitude: float
    longitude: float