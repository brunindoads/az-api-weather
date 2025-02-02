
# API de Clima

Esta API em Python, desenvolvida com Flask, consulta o clima atual com base no CEP informado, utilizando serviços gratuitos: [ViaCEP](https://viacep.com.br/), [Nominatim](https://nominatim.org/) e [Open-Meteo](https://open-meteo.com/). A documentação interativa da API é gerada com Swagger (via [Flasgger](https://github.com/flasgger/flasgger)) e está disponível na rota raiz.

## Funcionalidades

- **Consulta de endereço por CEP**: Utiliza a API gratuita do ViaCEP.
- **Geocodificação**: Obtém as coordenadas (latitude e longitude) do endereço usando Nominatim.
- **Consulta do clima atual**: Obtém os dados climáticos com o Open-Meteo.
- **Documentação Interativa**: Swagger UI disponível na rota `/`.

## Pré-requisitos

- Python 3.7 ou superior
- [pip](https://pip.pypa.io/en/stable/installation/)
- Ambiente virtual (recomendado)

## Instalação

1. **Clone o repositório (ou crie a pasta do projeto):**
   ```bash
   git clone <URL-do-seu-repositorio>
   cd api-weather
   ```

2. **Crie e ative o ambiente virtual:**

   No **Windows**:
   ```bash
   python -m venv venv
   venv\Scriptsctivate
   ```

   No **Linux/Mac**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## Arquivos do Projeto

- **`app.py`**: Código principal da API.
- **`requirements.txt`**: Lista de dependências do projeto.
- **`README.md`**: Este arquivo.

## Como Usar

1. **Execute a API localmente:**
   ```bash
   python app.py
   ```

2. **Acesse a documentação interativa (Swagger UI):**
   Abra o navegador e acesse:
   ```
   http://127.0.0.1:8000/
   ```

3. **Consultar o Clima:**
   Utilize o endpoint para consultar o clima passando um CEP:
   ```
   http://127.0.0.1:8000/weather/<CEP>
   ```
   *Exemplo:*
   ```
   http://127.0.0.1:8000/weather/01001000
   ```

## Teste na Azure

A API já está implantada no Azure App Service. Você pode testá-la acessando o seguinte link:

[https://weather-api-dio.azurewebsites.net/weather/95590000](https://weather-api-dio.azurewebsites.net/weather/95590000)

## Deploy no Azure

Para fazer o deploy da API no Azure App Service utilizando o VS Code:

1. **Instale as Extensões Necessárias:**
   - [Azure App Service](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azureappservice)
   - [Azure Account](https://marketplace.visualstudio.com/items?itemName=ms-vscode.azure-account)

2. **Crie um novo App Service:**
   - Abra a paleta de comandos (`Ctrl + Shift + P`).
   - Selecione **"Azure App Service: Create New Web App..."**.
   - Siga as instruções, escolhendo o runtime **Python** apropriado e um plano (por exemplo, o **F1 Free** para testes).

3. **Deploy:**
   - Clique com o botão direito no App Service criado na aba do Azure no VS Code.
   - Selecione **"Deploy to Web App"** e escolha a pasta do projeto (`api-weather`).

## Licença

Este projeto é open-source e pode ser usado conforme os termos da licença MIT.

---

*Desenvolvido com ♥ por [Seu Nome](mailto:seu_email@exemplo.com).*
