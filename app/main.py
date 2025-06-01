from fastapi import FastAPI, HTTPException
from app.schemas import Coordenadas
from typing import Dict, Any
from app.services.clima_service import ClimaService

app = FastAPI(
    title="Clima por Localização API",
    description="API para obtenção de dados climáticos baseados na localização do usuário",
    version="1.0.0"
)

clima_service = ClimaService()

@app.post("/clima/por-coordenadas", response_model=Dict[str, Any])
async def obter_clima_por_coordenadas(coordenadas: Coordenadas):
    try:
        return clima_service.obter_dados_climaticos(coordenadas)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))