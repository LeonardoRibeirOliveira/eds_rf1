import requests
from app.schemas import Coordenadas
from app.config import settings

class ClimaService:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    
    def obter_dados_climaticos(self, coordenadas: Coordenadas):
        params = {
            'lat': coordenadas.latitude,
            'lon': coordenadas.longitude,
            'appid': settings.OPENWEATHER_API_KEY,
            'units': 'metric',
            'lang': 'pt' 
        }
        
        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()
            
            return data
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro ao acessar a API de clima: {str(e)}")