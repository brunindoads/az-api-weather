from flask import Flask, jsonify
import requests
from flasgger import Swagger

app = Flask(__name__)

# Configuração para que o Swagger UI seja servido na rota "/"
app.config['SWAGGER'] = {
    'title': 'API de Clima',
    'uiversion': 3,
    'specs_route': '/'
}

swagger = Swagger(app)

@app.route('/weather/<cep>', methods=['GET'])
def get_weather(cep):
    """
    Retorna os dados do clima com base no CEP informado.
    ---
    parameters:
      - name: cep
        in: path
        type: string
        required: true
        description: CEP para a consulta de clima.
    responses:
      200:
        description: Dados do clima retornados com sucesso.
        schema:
          id: Weather
          properties:
            cep:
              type: string
              description: CEP informado.
            address:
              type: object
              properties:
                city:
                  type: string
                  description: Cidade obtida pelo ViaCEP.
                state:
                  type: string
                  description: Estado obtido pelo ViaCEP.
            coordinates:
              type: object
              properties:
                latitude:
                  type: string
                  description: Latitude obtida pelo Nominatim.
                longitude:
                  type: string
                  description: Longitude obtida pelo Nominatim.
            current_weather:
              type: object
              description: Dados do clima atual retornados pelo Open-Meteo.
      400:
        description: Erro na consulta dos dados.
    """
    # 1. Obter o endereço a partir do CEP com ViaCEP
    viacep_url = f"https://viacep.com.br/ws/{cep}/json/"
    response_viacep = requests.get(viacep_url)
    
    if response_viacep.status_code != 200:
        return jsonify({"error": "Erro ao obter dados de endereço pelo CEP."}), 400

    address_data = response_viacep.json()
    
    if "erro" in address_data:
        return jsonify({"error": "CEP não encontrado."}), 404

    city = address_data.get("localidade")
    state = address_data.get("uf")
    
    if not city or not state:
        return jsonify({"error": "Dados de endereço incompletos."}), 400

    # 2. Obter as coordenadas com Nominatim (OpenStreetMap)
    nominatim_url = "https://nominatim.openstreetmap.org/search"
    query = f"{city}, {state}, Brazil"
    params = {
        "q": query,
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "api-weather-app (seu_email@exemplo.com)"  # Substitua pelo seu e-mail
    }
    response_nominatim = requests.get(nominatim_url, params=params, headers=headers)
    
    if response_nominatim.status_code != 200:
        return jsonify({"error": "Erro ao obter coordenadas do endereço."}), 400
    
    nominatim_data = response_nominatim.json()
    if not nominatim_data:
        return jsonify({"error": "Coordenadas não encontradas para o CEP informado."}), 404

    lat = nominatim_data[0].get("lat")
    lon = nominatim_data[0].get("lon")
    
    if not lat or not lon:
        return jsonify({"error": "Coordenadas não disponíveis."}), 400

    # 3. Obter dados do clima com Open-Meteo
    open_meteo_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "timezone": "America/Sao_Paulo"
    }
    response_weather = requests.get(open_meteo_url, params=params)
    if response_weather.status_code != 200:
        return jsonify({"error": "Erro ao obter dados do clima."}), 400

    weather_data = response_weather.json()
    current_weather = weather_data.get("current_weather")
    
    if not current_weather:
        return jsonify({"error": "Dados de clima não disponíveis."}), 400

    result = {
        "cep": cep,
        "address": {
            "city": city,
            "state": state
        },
        "coordinates": {
            "latitude": lat,
            "longitude": lon
        },
        "current_weather": current_weather
    }
    
    return jsonify(result)

if __name__ == '__main__':
    # No Windows, ative o ambiente virtual com: venv\Scripts\activate
    app.run(host='0.0.0.0', port=8000)
